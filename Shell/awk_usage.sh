#!/bin/bash

echo ## printで出力
echo "## awk '{ print }' sample.txt ##"
awk '{ print }' sample.txt
echo ""

echo "## printfで出力"
echo "## awk '{ printf "%s %s %s", \$1, \$2, \$3 }' sample.txt ##"
awk '{ printf "%s %s %s", $1, $2, $3 }' sample.txt
echo ""
echo ""

echo "## 特定の列を出力"
echo "## awk '{ print $3, $5 }' sample.txt ##"
awk '{ print $3, $5 }' sample.txt
echo ""

echo "## 行を指定して、出力"
echo "## awk 'NR==1; NR==3' sample.txt"
awk 'NR==1; NR==3' sample.txt
echo ""

echo "## 特定の文字列を含む行を取得"
echo "## awk '/B/' sample.txt"
awk '/B/' sample.txt
echo ""