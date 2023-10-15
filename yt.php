<?php
// Function to extract M3U8 URLs from a webpage and redirect
function extractM3U8Urls($url) {
    $content = file_get_contents($url);

    // Extract the hlsManifestUrl value
    $matches = [];
    if (preg_match('/"hlsManifestUrl":"(https:\/\/[^"]+)"/', $content, $matches)) {
        $m3u8Url = $matches[1];
        // Redirect to the M3U8 URL
        header("Location: $m3u8Url");
        exit; // Ensure script execution stops after the redirect
    } else {
        echo "M3U8 URL not found in the content.";
    }
}

// Check if a URL argument was provided
if (isset($_GET['url'])) {
    $url = $_GET['url'];
    extractM3U8Urls($url);
} else {
    echo "URL parameter missing.";
}
?>
