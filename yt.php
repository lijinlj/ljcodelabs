<?php
// Replace this with the URL of the webpage you want to extract M3U8 URLs from
$url = 'https://www.youtube.com/watch?v=V_MXWptocIE';

// Function to extract M3U8 URLs from a webpage
function extractM3U8Urls($url) {
    $content = file_get_contents($url);

    // Use a regular expression to find M3U8 URLs
    $pattern = '/(https?:\/\/.*\.m3u8)/i';
    preg_match_all($pattern, $content, $matches);

    return $matches[0];
}

// Get and print M3U8 URLs
$m3u8Urls = extractM3U8Urls($url);
foreach ($m3u8Urls as $url) {
    echo $url . "\n";
}
?>
