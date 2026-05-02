import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';

class SettingsScreen extends ConsumerWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final themeMode = ref.watch(themeModeProvider);
    final settings = ref.watch(settingsProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Settings'),
      ),
      body: ListView(
        children: [
          // Appearance Section
          _buildSectionHeader(context, 'Appearance'),
          _buildThemeSelector(context, ref, themeMode),
          const Divider(),

          // Storage Section
          _buildSectionHeader(context, 'Storage'),
          SwitchListTile(
            title: const Text('Auto-delete processed files'),
            subtitle: const Text('Remove files after 24 hours'),
            value: settings.autoDeleteFiles,
            onChanged: (value) {
              ref.read(settingsProvider.notifier).setAutoDelete(value);
            },
          ),
          ListTile(
            title: const Text('Storage location'),
            subtitle: Text(settings.storageLocation == 'internal'
                ? 'Internal storage'
                : 'SD Card'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () => _showStorageLocationDialog(context, ref, settings.storageLocation),
          ),
          const Divider(),

          // About Section
          _buildSectionHeader(context, 'About'),
          ListTile(
            leading: const Icon(Icons.info_outline),
            title: const Text('App Version'),
            subtitle: const Text('1.0.0'),
          ),
          ListTile(
            leading: const Icon(Icons.privacy_tip_outlined),
            title: const Text('Privacy Policy'),
            trailing: const Icon(Icons.open_in_new, size: 18),
            onTap: () {
              // Open privacy policy
            },
          ),
          ListTile(
            leading: const Icon(Icons.help_outline),
            title: const Text('Help & Support'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {
              // Open help
            },
          ),
          ListTile(
            leading: const Icon(Icons.mail_outline),
            title: const Text('Contact Us'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {
              // Open contact
            },
          ),
          const Divider(),

          // Rate & Share
          _buildSectionHeader(context, 'Rate & Share'),
          ListTile(
            leading: const Icon(Icons.star_outline),
            title: const Text('Rate Us'),
            subtitle: const Text('Love using LovePDFs? Rate us 5 stars!'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {
              // Open app store for rating
            },
          ),
          ListTile(
            leading: const Icon(Icons.share_outlined),
            title: const Text('Share App'),
            subtitle: const Text('Share with friends and family'),
            trailing: const Icon(Icons.chevron_right),
            onTap: () {
              // Share app
            },
          ),
        ],
      ),
    );
  }

  Widget _buildSectionHeader(BuildContext context, String title) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 24, 16, 8),
      child: Text(
        title,
        style: Theme.of(context).textTheme.titleSmall?.copyWith(
          color: AppColors.primary,
          fontWeight: FontWeight.bold,
          letterSpacing: 1,
        ),
      ),
    );
  }

  Widget _buildThemeSelector(BuildContext context, WidgetRef ref, ThemeMode currentMode) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Padding(
            padding: EdgeInsets.only(left: 4, bottom: 8),
            child: Text(
              'Theme',
              style: TextStyle(fontSize: 16),
            ),
          ),
          SegmentedButton<ThemeMode>(
            segments: const [
              ButtonSegment(
                value: ThemeMode.light,
                label: Text('Light'),
                icon: Icon(Icons.light_mode),
              ),
              ButtonSegment(
                value: ThemeMode.system,
                label: Text('Auto'),
                icon: Icon(Icons.brightness_auto),
              ),
              ButtonSegment(
                value: ThemeMode.dark,
                label: Text('Dark'),
                icon: Icon(Icons.dark_mode),
              ),
            ],
            selected: {currentMode},
            onSelectionChanged: (value) {
              ref.read(themeModeProvider.notifier).state = value.first;
            },
          ),
        ],
      ),
    );
  }

  void _showStorageLocationDialog(BuildContext context, WidgetRef ref, String current) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Storage Location'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            RadioListTile<String>(
              title: const Text('Internal Storage'),
              subtitle: const Text('Store in device internal memory'),
              value: 'internal',
              groupValue: current,
              onChanged: (value) {
                ref.read(settingsProvider.notifier).setStorageLocation(value!);
                Navigator.pop(context);
              },
            ),
            RadioListTile<String>(
              title: const Text('SD Card'),
              subtitle: const Text('Store on external SD card if available'),
              value: 'sdcard',
              groupValue: current,
              onChanged: (value) {
                ref.read(settingsProvider.notifier).setStorageLocation(value!);
                Navigator.pop(context);
              },
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Cancel'),
          ),
        ],
      ),
    );
  }
}
