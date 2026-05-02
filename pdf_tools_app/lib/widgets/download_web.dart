import 'dart:html' as html;
import 'dart:typed_data';

/// Web-specific download implementation using AnchorElement
void downloadFileWeb(Uint8List bytes, String fileName, String mimeType) {
  // Create a blob from the bytes
  final blob = html.Blob([bytes], mimeType);
  
  // Create an object URL
  final url = html.Url.createObjectUrlFromBlob(blob);
  
  // Create an anchor element and trigger download
  final anchor = html.AnchorElement()
    ..href = url
    ..download = fileName
    ..style.display = 'none';
  
  // Add to document, click, and remove
  html.document.body?.children.add(anchor);
  anchor.click();
  html.document.body?.children.remove(anchor);
  
  // Revoke the object URL
  html.Url.revokeObjectUrl(url);
}

/// On web, mobile download is not supported - this is just a stub that throws
Future<void> downloadFileMobileDesktop({
  String? outputPath,
  Uint8List? outputBytes,
  required String outputFileName,
  required String ext,
}) async {
  throw UnsupportedError('Mobile/Desktop download is not supported on web platform');
}
