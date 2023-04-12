#!/usr/local/bin/ruby

require 'cgi'

def html_header
  return <<-EOF_HEADER
Content-Type: text/html

  <html>
  <title>simple calculator</title>
  <body>
   input:
EOF_HEADER
end

def html_footer
  return <<-EOF_FOOTER
  </html>
  </body>
EOF_FOOTER
end

def html_form
  return <<-EOF_FORM
  <form action="calc.cgi" method="post">
    <input name="exp" size="25" />
  </form>
EOF_FORM
end

################################################################
### main

content = []

params = CGI.new
exp = params['exp'].to_s

exp = exp.tr('０-９','0-9') #　全角入力もしたい？
exp = exp.gsub(" ", "") # 空白文字を削除するようにした

content << html_header

if exp =~ /^$/
  # initial state
  msg = ''
  content << msg << html_form

elsif exp =~ /\A(\d+([\/*%+-]|\*\*))+\d+\z/ # 正規表現を改良し、演算子で終わるような式がマッチしないようにした。
  # got user input
  msg = eval exp
  content << exp << '=' << msg << html_form # 表示する際に、元の式を見れるようにした

else
  # invalid input
  msg = 'invalid expression.'
  content << msg << html_form
end

content << html_footer

print content.join