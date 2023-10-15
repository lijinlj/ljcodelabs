<?php
// Replace this with the URL of the webpage you want to extract M3U8 URLs from
$url = 'https://www.youtube.com/watch?v=V_MXWptocIE';

// Function to extract M3U8 URLs from a webpage
function extractM3U8Urls($url) {
    $content = file_get_contents($url);

    // Extract the hlsManifestUrl value
    $matches = [];
    if (preg_match('/"hlsManifestUrl":"(https:\/\/[^"]+)"/', $content, $matches)) {
        $m3u8Url = $matches[1];
        echo $m3u8Url;
    } else {
        echo "M3U8 URL not found in the content.";
    }
   
    return $m3u8Url;
}

// Get and print M3U8 URLs
$m3u8Urls = extractM3U8Urls($url);
foreach ($m3u8Urls as $url) {
    echo $url . "\n";
}
?>
