import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/app_tool.dart';

// Theme Provider
final themeModeProvider = StateProvider<ThemeMode>((ref) => ThemeMode.light);

// Selected Tool Provider
final selectedToolProvider = StateProvider<AppTool?>((ref) => null);

// Search Query Provider
final searchQueryProvider = StateProvider<String>((ref) => '');

// Filtered Tools Provider
final filteredToolsProvider = Provider<List<AppTool>>((ref) {
  final query = ref.watch(searchQueryProvider);
  if (query.isEmpty) {
    return p0Tools;
  }
  return searchTools(query);
});

// Tools by Category Provider
final toolsByCategoryProvider = Provider.family<List<AppTool>, ToolCategory>((ref, category) {
  return getToolsByCategory(category);
});

// Selected Category Provider
final selectedCategoryProvider = StateProvider<ToolCategory?>((ref) => null);

// Favorite Tools Provider
final favoriteToolsProvider = StateNotifierProvider<FavoriteToolsNotifier, List<String>>((ref) {
  return FavoriteToolsNotifier();
});

class FavoriteToolsNotifier extends StateNotifier<List<String>> {
  FavoriteToolsNotifier() : super([]);

  void toggleFavorite(String toolId) {
    if (state.contains(toolId)) {
      state = state.where((id) => id != toolId).toList();
    } else {
      state = [...state, toolId];
    }
  }

  bool isFavorite(String toolId) {
    return state.contains(toolId);
  }
}

// Recent Files Provider
final recentFilesProvider = StateNotifierProvider<RecentFilesNotifier, List<RecentFile>>((ref) {
  return RecentFilesNotifier();
});

class RecentFile {
  final String id;
  final String fileName;
  final String toolId;
  final String toolName;
  final DateTime date;
  final int fileSize;
  final String? thumbnailPath;

  RecentFile({
    required this.id,
    required this.fileName,
    required this.toolId,
    required this.toolName,
    required this.date,
    required this.fileSize,
    this.thumbnailPath,
  });
}

class RecentFilesNotifier extends StateNotifier<List<RecentFile>> {
  RecentFilesNotifier() : super([]);

  void addFile(RecentFile file) {
    // Keep only last 20 files
    final newState = [file, ...state];
    if (newState.length > 20) {
      state = newState.sublist(0, 20);
    } else {
      state = newState;
    }
  }

  void removeFile(String id) {
    state = state.where((file) => file.id != id).toList();
  }

  void clearFiles() {
    state = [];
  }
}

// Processing State Provider
final processingStateProvider = StateNotifierProvider.family<ProcessingStateNotifier, ProcessingState, String>((ref, toolId) {
  return ProcessingStateNotifier();
});

enum ProcessingStatus { idle, picking, uploading, processing, completed, error }

class ProcessingState {
  final ProcessingStatus status;
  final String? message;
  final double progress;
  final String? outputPath;
  final Uint8List? outputBytes;
  final String? error;

  ProcessingState({
    this.status = ProcessingStatus.idle,
    this.message,
    this.progress = 0.0,
    this.outputPath,
    this.outputBytes,
    this.error,
  });

  ProcessingState copyWith({
    ProcessingStatus? status,
    String? message,
    double? progress,
    String? outputPath,
    Uint8List? outputBytes,
    String? error,
  }) {
    return ProcessingState(
      status: status ?? this.status,
      message: message ?? this.message,
      progress: progress ?? this.progress,
      outputPath: outputPath ?? this.outputPath,
      outputBytes: outputBytes ?? this.outputBytes,
      error: error ?? this.error,
    );
  }
}

class ProcessingStateNotifier extends StateNotifier<ProcessingState> {
  ProcessingStateNotifier() : super(ProcessingState());

  void startPicking() {
    state = state.copyWith(
      status: ProcessingStatus.picking,
      message: 'Selecting files...',
    );
  }

  void startUpload() {
    state = state.copyWith(
      status: ProcessingStatus.uploading,
      message: 'Uploading files...',
      progress: 0.0,
    );
  }

  void updateProgress(double progress) {
    state = state.copyWith(progress: progress);
  }

  void startProcessing() {
    state = state.copyWith(
      status: ProcessingStatus.processing,
      message: 'Processing...',
    );
  }

  void complete(String outputPath, {Uint8List? outputBytes}) {
    state = state.copyWith(
      status: ProcessingStatus.completed,
      message: 'Completed!',
      progress: 1.0,
      outputPath: outputPath,
      outputBytes: outputBytes,
    );
  }

  void setError(String error) {
    state = state.copyWith(
      status: ProcessingStatus.error,
      message: 'Error occurred',
      error: error,
    );
  }

  void reset() {
    state = ProcessingState();
  }
}

// Selected Files Provider
final selectedFilesProvider = StateNotifierProvider<SelectedFilesNotifier, List<SelectedFile>>((ref) {
  return SelectedFilesNotifier();
});

class SelectedFile {
  final String id;
  final String? path;
  final Uint8List? bytes;
  final String name;
  final int size;
  final String extension;

  SelectedFile({
    required this.id,
    this.path,
    this.bytes,
    required this.name,
    required this.size,
    required this.extension,
  });

  bool get isWeb => bytes != null && path == null;
}

class SelectedFilesNotifier extends StateNotifier<List<SelectedFile>> {
  SelectedFilesNotifier() : super([]);

  void addFile(SelectedFile file) {
    state = [...state, file];
  }

  void removeFile(String id) {
    state = state.where((file) => file.id != id).toList();
  }

  void reorderFiles(int oldIndex, int newIndex) {
    if (oldIndex < newIndex) {
      newIndex -= 1;
    }
    final item = state.removeAt(oldIndex);
    state = [
      ...state.sublist(0, newIndex),
      item,
      ...state.sublist(newIndex),
    ];
  }

  void clearFiles() {
    state = [];
  }
}

// Navigation Index Provider
final navigationIndexProvider = StateProvider<int>((ref) => 0);

// Language Provider
final languageProvider = StateProvider<String>((ref) => 'en');

// Settings Provider
final settingsProvider = StateNotifierProvider<SettingsNotifier, AppSettings>((ref) {
  return SettingsNotifier();
});

class AppSettings {
  final bool autoDeleteFiles;
  final String storageLocation;
  final int successfulUsesCount;

  AppSettings({
    this.autoDeleteFiles = false,
    this.storageLocation = 'internal',
    this.successfulUsesCount = 0,
  });

  AppSettings copyWith({
    bool? autoDeleteFiles,
    String? storageLocation,
    int? successfulUsesCount,
  }) {
    return AppSettings(
      autoDeleteFiles: autoDeleteFiles ?? this.autoDeleteFiles,
      storageLocation: storageLocation ?? this.storageLocation,
      successfulUsesCount: successfulUsesCount ?? this.successfulUsesCount,
    );
  }
}

class SettingsNotifier extends StateNotifier<AppSettings> {
  SettingsNotifier() : super(AppSettings());

  void setAutoDelete(bool value) {
    state = state.copyWith(autoDeleteFiles: value);
  }

  void setStorageLocation(String location) {
    state = state.copyWith(storageLocation: location);
  }

  void incrementSuccessfulUse() {
    state = state.copyWith(successfulUsesCount: state.successfulUsesCount + 1);
  }
}
