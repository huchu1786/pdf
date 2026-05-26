import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import '../models/quiz_history.dart';

class PdfService {
  static Future<void> generateAndPrintCertificate(QuizAttempt attempt, String userName) async {
    final pdf = await generateCertificate(attempt, userName);
    await Printing.layoutPdf(
      onLayout: (PdfPageFormat format) async => pdf.save(),
      name: 'Certificate_${attempt.quizTitle.replaceAll(' ', '_')}.pdf',
    );
  }

  static Future<pw.Document> generateCertificate(QuizAttempt attempt, String userName) async {
    final pdf = pw.Document();

    final dateStr = "${attempt.date.day}/${attempt.date.month}/${attempt.date.year}";
    final scorePercentage = attempt.percentage.toStringAsFixed(1);

    // Let's load the font
    final font = await PdfGoogleFonts.outfitRegular();
    final fontBold = await PdfGoogleFonts.outfitBold();

    pdf.addPage(
      pw.Page(
        pageFormat: PdfPageFormat.a4.landscape,
        build: (pw.Context context) {
          return pw.FullPage(
            ignoreMargins: true,
            child: pw.Container(
              decoration: const pw.BoxDecoration(
                gradient: pw.LinearGradient(
                  colors: [
                    PdfColor.fromInt(0xFF0F0C1B),
                    PdfColor.fromInt(0xFF1E143E),
                  ],
                  begin: pw.Alignment.topLeft,
                  end: pw.Alignment.bottomRight,
                ),
              ),
              child: pw.Stack(
                children: [
                  // Decorative outer border
                  pw.Positioned.fill(
                    child: pw.Container(
                      margin: const pw.EdgeInsets.all(30),
                      decoration: pw.BoxDecoration(
                        border: pw.Border.all(
                          color: const PdfColor.fromInt(0xFFD4AF37), // Metallic Gold
                          width: 4,
                        ),
                        borderRadius: const pw.BorderRadius.all(pw.Radius.circular(8)),
                      ),
                    ),
                  ),
                  // Inner slim gold border
                  pw.Positioned.fill(
                    child: pw.Container(
                      margin: const pw.EdgeInsets.all(40),
                      decoration: pw.BoxDecoration(
                        border: pw.Border.all(
                          color: const PdfColor.fromInt(0xFFF9E7B9),
                          width: 1.5,
                        ),
                        borderRadius: const pw.BorderRadius.all(pw.Radius.circular(6)),
                      ),
                    ),
                  ),
                  // Corner decoration accents
                  _buildCornerDecoration(top: 45, left: 45, size: 20),
                  _buildCornerDecoration(top: 45, right: 45, size: 20),
                  _buildCornerDecoration(bottom: 45, left: 45, size: 20),
                  _buildCornerDecoration(bottom: 45, right: 45, size: 20),

                  // Certificate content
                  pw.Center(
                    child: pw.Padding(
                      padding: const pw.EdgeInsets.symmetric(horizontal: 60, vertical: 50),
                      child: pw.Column(
                        mainAxisAlignment: pw.MainAxisAlignment.center,
                        children: [
                          // Top Ribbon Header
                          pw.Text(
                            'CERTIFICATE OF COMPLETION',
                            style: pw.TextStyle(
                              font: fontBold,
                              fontSize: 28,
                              color: const PdfColor.fromInt(0xFFD4AF37),
                              letterSpacing: 2.0,
                            ),
                          ),
                          pw.SizedBox(height: 10),
                          pw.Container(
                            width: 120,
                            height: 2,
                            color: const PdfColor.fromInt(0xFF00F5FF),
                          ),
                          pw.SizedBox(height: 25),

                          pw.Text(
                            'THIS IS PROUDLY PRESENTED TO',
                            style: pw.TextStyle(
                              font: font,
                              fontSize: 10,
                              color: const PdfColor.fromInt(0xFFA0A5C1),
                              letterSpacing: 1.5,
                            ),
                          ),
                          pw.SizedBox(height: 15),

                          pw.Text(
                            userName.toUpperCase(),
                            style: pw.TextStyle(
                              font: fontBold,
                              fontSize: 32,
                              color: PdfColors.white,
                              letterSpacing: 1.0,
                            ),
                          ),
                          pw.SizedBox(height: 15),

                          pw.Text(
                            'for successfully completing the specialized quiz assessment:',
                            style: pw.TextStyle(
                              font: font,
                              fontSize: 12,
                              color: const PdfColor.fromInt(0xFFA0A5C1),
                            ),
                          ),
                          pw.SizedBox(height: 10),

                          // Quiz Title Card
                          pw.Text(
                            '"${attempt.quizTitle}"',
                            style: pw.TextStyle(
                              font: fontBold,
                              fontSize: 22,
                              color: const PdfColor.fromInt(0xFF00F5FF),
                            ),
                          ),
                          pw.SizedBox(height: 20),

                          // Scoring & Date details
                          pw.Row(
                            mainAxisAlignment: pw.MainAxisAlignment.center,
                            children: [
                              pw.Column(
                                children: [
                                  pw.Text(
                                    'SCORE ACCURACY',
                                    style: pw.TextStyle(
                                      font: font,
                                      fontSize: 9,
                                      color: const PdfColor.fromInt(0xFFA0A5C1),
                                      letterSpacing: 1,
                                    ),
                                  ),
                                  pw.SizedBox(height: 4),
                                  pw.Text(
                                    '$scorePercentage%',
                                    style: pw.TextStyle(
                                      font: fontBold,
                                      fontSize: 18,
                                      color: const PdfColor.fromInt(0xFF00FF87),
                                    ),
                                  ),
                                ],
                              ),
                              pw.SizedBox(width: 60),
                              pw.Column(
                                children: [
                                  pw.Text(
                                    'DATE ISSUED',
                                    style: pw.TextStyle(
                                      font: font,
                                      fontSize: 9,
                                      color: const PdfColor.fromInt(0xFFA0A5C1),
                                      letterSpacing: 1,
                                    ),
                                  ),
                                  pw.SizedBox(height: 4),
                                  pw.Text(
                                    dateStr,
                                    style: pw.TextStyle(
                                      font: fontBold,
                                      fontSize: 18,
                                      color: PdfColors.white,
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                          pw.SizedBox(height: 35),

                          // Signature/Verification Area
                          pw.Row(
                            mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                            children: [
                              pw.Column(
                                children: [
                                  pw.Container(
                                    width: 140,
                                    height: 1,
                                    color: const PdfColor.fromInt(0x33FFFFFF),
                                  ),
                                  pw.SizedBox(height: 4),
                                  pw.Text(
                                    'ASSESSOR SIGNATURE',
                                    style: pw.TextStyle(
                                      font: font,
                                      fontSize: 8,
                                      color: const PdfColor.fromInt(0xFFA0A5C1),
                                    ),
                                  ),
                                ],
                              ),
                              // Emblem Icon (simulated via decorative border and shapes)
                              pw.Container(
                                width: 50,
                                height: 50,
                                decoration: pw.BoxDecoration(
                                  shape: pw.BoxShape.circle,
                                  border: pw.Border.all(
                                    color: const PdfColor.fromInt(0xFFD4AF37),
                                    width: 2,
                                  ),
                                  color: const PdfColor.fromInt(0xFF1E143E),
                                ),
                                child: pw.Center(
                                  child: pw.Text(
                                    'Q',
                                    style: pw.TextStyle(
                                      font: fontBold,
                                      fontSize: 24,
                                      color: const PdfColor.fromInt(0xFFD4AF37),
                                    ),
                                  ),
                                ),
                              ),
                              pw.Column(
                                children: [
                                  pw.Container(
                                    width: 140,
                                    height: 1,
                                    color: const PdfColor.fromInt(0x33FFFFFF),
                                  ),
                                  pw.SizedBox(height: 4),
                                  pw.Text(
                                    'QUIZPRO SYSTEM VERIFIED',
                                    style: pw.TextStyle(
                                      font: font,
                                      fontSize: 8,
                                      color: const PdfColor.fromInt(0xFFA0A5C1),
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );

    return pdf;
  }

  static pw.Widget _buildCornerDecoration({
    double? top,
    double? bottom,
    double? left,
    double? right,
    required double size,
  }) {
    return pw.Positioned(
      top: top,
      bottom: bottom,
      left: left,
      right: right,
      child: pw.Container(
        width: size,
        height: size,
        decoration: pw.BoxDecoration(
          border: pw.Border(
            top: top != null ? const pw.BorderSide(color: PdfColor.fromInt(0xFFD4AF37), width: 3) : pw.BorderSide.none,
            bottom: bottom != null ? const pw.BorderSide(color: PdfColor.fromInt(0xFFD4AF37), width: 3) : pw.BorderSide.none,
            left: left != null ? const pw.BorderSide(color: PdfColor.fromInt(0xFFD4AF37), width: 3) : pw.BorderSide.none,
            right: right != null ? const pw.BorderSide(color: PdfColor.fromInt(0xFFD4AF37), width: 3) : pw.BorderSide.none,
          ),
        ),
      ),
    );
  }
}
