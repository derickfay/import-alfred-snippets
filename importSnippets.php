#!/usr/bin/env php
<?php

/**
 * importSnippets.php
 *
 * generates Alfred 3 json snippets from a csv file
 *
 * written for php 7.4
 */

$sourceFile = 'snippets.csv';
$fieldNames = ['name', 'keyword', 'content'];

if (($reader = fopen($sourceFile, 'r')) !== FALSE) {
    while (($row = fgetcsv($reader, 1000)) !== FALSE) {
        $row = array_combine($fieldNames, $row);
        $uid = vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex(implode('', $row)), 4));
        $output = json_encode([
            'alfredsnippet' => [
                'snippet' => $row['content'],
                'uid' => $uid,
                'name' => $row['name'],
                'keyword' => $row['keyword'],
            ]
        ], JSON_PRETTY_PRINT);
        $safeName = trim(preg_replace('/[^[:alnum:]]+/', ' ', $row['name']));
        $safeName = trim(preg_replace('/\s+/', ' ', $safeName));
        $outputFile = $safeName.' ['.$uid.'].json';
        file_put_contents($outputFile, $output);
    }
    fclose($reader);
}
