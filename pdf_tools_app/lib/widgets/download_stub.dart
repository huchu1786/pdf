import 'dart:typed_data';

/// Stub for web download - will be replaced by download_web.dart on web platform
void downloadFileWeb(Uint8List bytes, String fileName, String mimeType) {
  throw UnsupportedError('Web download is not supported on this platform');
}

/// Stub for mobile/desktop download - will be replaced on mobile/desktop platforms
Future<void> downloadFileMobileDesktop({
  String? outputPath,
  Uint8List? outputBytes,
  required String outputFileName,
  required String ext,
}) async {
  throw UnsupportedError('Mobile/Desktop download is not supported on this platform');
}
