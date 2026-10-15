"""Source-level privacy contracts; Android build/device tests are separate gates."""
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ANDROID = "{http://schemas.android.com/apk/res/android}"
DOMAINS = {"root", "file", "database", "sharedpref", "external", "device_root", "device_file", "device_database", "device_sharedpref"}


class PrivacyContracts(unittest.TestCase):
    def test_system_backup_is_disabled(self):
        app = ET.parse(ROOT / "app/src/main/AndroidManifest.xml").find("application")
        self.assertEqual(app.get(ANDROID + "allowBackup"), "false")
        self.assertEqual(app.get(ANDROID + "fullBackupContent"), "@xml/ghostweb_backup_rules")
        self.assertEqual(app.get(ANDROID + "dataExtractionRules"), "@xml/ghostweb_data_extraction_rules")

    def test_all_storage_domains_are_excluded(self):
        legacy = ET.parse(ROOT / "app/src/main/res/xml/ghostweb_backup_rules.xml").getroot()
        modern = ET.parse(ROOT / "app/src/main/res/xml/ghostweb_data_extraction_rules.xml").getroot()
        for section in [legacy, modern.find("cloud-backup"), modern.find("device-transfer")]:
            self.assertIsNotNone(section)
            self.assertFalse(section.findall("include"))
            self.assertEqual({(e.get("domain"), e.get("path")) for e in section.findall("exclude")}, {(d, ".") for d in DOMAINS})

    def test_privacy_screen_is_reachable(self):
        nav = ET.parse(ROOT / "app/src/main/res/navigation/privacy_settings.xml").getroot()
        destination = "@+id/graphenePrivacySettingsFragment"
        self.assertTrue(any(e.get(ANDROID + "id") == destination for e in nav.findall("fragment")))
        parent = next(e for e in nav.findall("fragment") if e.get(ANDROID + "id") == "@+id/privacySettingsFragment")
        app_ns = "{http://schemas.android.com/apk/res-auto}"
        self.assertTrue(any(e.get(app_ns + "destination") == "@id/graphenePrivacySettingsFragment" for e in parent.findall("action")))


if __name__ == "__main__":
    unittest.main()
