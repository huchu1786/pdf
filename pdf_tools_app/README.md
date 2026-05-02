# LovePDFs Flutter App

A comprehensive PDF and image processing mobile application built with Flutter for LovePDFs.in platform.

## Features

### PDF Tools (P0 - MVP)
- **Merge PDF** - Combine multiple PDF files into one
- **Split PDF** - Split PDF by page ranges or extract individual pages
- **Compress PDF** - Reduce PDF file size
- **PDF to Word** - Convert PDF to editable DOCX
- **PDF to Excel** - Convert PDF tables to XLSX
- **Word to PDF** - Convert DOCX to PDF
- **JPG to PDF** - Convert JPG images to PDF
- **Image to PDF** - Convert any image to PDF
- **PDF to JPG** - Convert PDF pages to JPG images
- **PDF to Image** - Convert PDF to PNG/WebP

### Image Tools (P0 - MVP)
- **Compress Image** - Reduce image file size
- **Compress to 100KB** - Compress to exactly 100KB
- **Compress to 20KB** - Compress to exactly 20KB (perfect for government forms)
- **Crop Image** - Crop with presets (passport size, social media)
- **Resize Image** - Resize by pixels or percentage
- **Rotate Image** - Rotate 90°, 180°, 270°
- **Convert to JPG** - Convert any image to JPG
- **Convert from JPG** - Convert JPG to PNG/WebP

### Other Tools (P0 - MVP)
- **QR Code Generator** - Generate QR codes for text/URLs

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Flutter 3.x |
| Language | Dart |
| State Management | Riverpod 2.x |
| Local PDF Processing | syncfusion_flutter_pdf, pdf |
| Image Processing | image, flutter_image_compress |
| File Handling | file_picker, path_provider, share_plus |
| QR Generation | qr_flutter |
| UI/UX | Material 3, Google Fonts (Nunito) |

## Project Structure

```
lib/
├── main.dart                 # App entry point
├── models/
│   ├── app_tool.dart        # Tool definitions and data
│   └── tool_model.dart      # Legacy model (deprecated)
├── providers/
│   └── app_providers.dart   # Riverpod state management
├── screens/
│   ├── splash_screen.dart   # App launch screen
│   ├── main_screen.dart     # Main navigation shell
│   ├── home_screen.dart     # Tool grid and search
│   ├── tool_detail_screen.dart  # Individual tool interface
│   ├── recent_screen.dart   # Recent files history
│   ├── favorites_screen.dart # Favorite tools
│   └── settings_screen.dart # App settings
├── services/
│   ├── image_service.dart   # Local image processing
│   ├── pdf_service.dart     # Local PDF processing
│   ├── qr_service.dart      # QR code generation
│   └── tool_service.dart    # Legacy service (deprecated)
├── theme/
│   └── app_theme.dart       # App colors, typography, themes
└── widgets/
    ├── tool_card.dart       # Tool grid item
    ├── category_header.dart # Category section header
    ├── file_picker_section.dart # File selection UI
    ├── tool_info_section.dart # Tool instructions/features
    ├── processing_section.dart # Processing status UI
    └── result_section.dart  # Result/download UI
```

## Getting Started

### Prerequisites
- Flutter SDK 3.5.0 or higher
- Dart SDK 3.0.0 or higher
- Android Studio / Xcode (for emulators)
- VS Code with Flutter extension (recommended)

### Installation

1. **Clone the repository**
   ```bash
   cd pdf_tools_app
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Run the app**
   ```bash
   # For Android
   flutter run

   # For specific device
   flutter run -d <device_id>
   ```

### Building for Production

```bash
# Android APK
flutter build apk --release

# Android App Bundle
flutter build appbundle --release

# iOS
flutter build ios --release
```

## Configuration

### Android Permissions
The following permissions are already configured in `android/app/src/main/AndroidManifest.xml`:
- `INTERNET` - For API-based tools
- `READ_EXTERNAL_STORAGE` - For file picking
- `WRITE_EXTERNAL_STORAGE` - For saving processed files
- `ACCESS_MEDIA_LOCATION` - For accessing media files

### iOS Permissions
Add the following to `ios/Runner/Info.plist`:
```xml
<key>NSPhotoLibraryUsageDescription</key>
<string>This app needs access to photos to process images and PDFs</string>
<key>NSDocumentsFolderUsageDescription</key>
<string>This app needs access to documents to process PDFs</string>
```

## Architecture

### State Management
The app uses Riverpod for state management with the following providers:
- `themeModeProvider` - Light/Dark/System theme
- `favoriteToolsProvider` - User's favorite tools
- `recentFilesProvider` - Processing history
- `selectedFilesProvider` - Current file selection
- `processingStateProvider` - Tool processing status

### Processing Modes
- **Local Processing** (Image tools, QR generator) - Done on-device without internet
- **Cloud Processing** (PDF conversion tools) - Requires API connection to lovepdf.in backend

### File Storage
- Input files: Picked from device storage
- Output files: Saved to app documents directory (`/LovePDFs/output/`)
- Recent files: Metadata stored in memory (persist to SharedPreferences in production)

## API Integration (Future)

For backend-requiring tools, integrate with lovepdf.in API:

```dart
// Example API call structure
POST /api/merge-pdf
Content-Type: multipart/form-data

files: [file1.pdf, file2.pdf]
```

See PRD Section 11 for full API specifications.

## Customization

### Adding New Tools
1. Add tool definition to `lib/models/app_tool.dart`
2. Implement processing logic in appropriate service
3. Add tool-specific UI if needed

### Theming
Modify `lib/theme/app_theme.dart`:
- `AppColors` - Color palette
- `AppTheme.lightTheme` / `AppTheme.darkTheme` - Theme data
- `AppTextStyles` - Typography

## Known Limitations

1. **Image OCR** - Requires Tesseract or cloud API integration
2. **PDF to Word/Excel** - Requires backend API (currently simulated)
3. **File persistence** - Recent files not persisted across sessions (use SharedPreferences)
4. **iOS file system** - Limited access to device file system

## Roadmap

### Phase 1 (MVP - Current)
- [x] All P0 image tools (local processing)
- [x] P0 PDF tools UI structure
- [x] Basic file handling
- [x] Settings, Favorites, Recent screens

### Phase 2 (v1.1)
- [ ] Backend API integration
- [ ] Hindi language support
- [ ] File persistence with SharedPreferences
- [ ] In-app review prompts

### Phase 3 (v1.2)
- [ ] Firebase integration (Analytics, Crashlytics)
- [ ] AdMob integration
- [ ] Premium subscription
- [ ] Cloud history sync

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is proprietary to LovePDFs.in

## Support

For support, email support@lovepdf.in or visit https://lovepdf.in/contact

---

Built with ❤️ by the LovePDFs Team
