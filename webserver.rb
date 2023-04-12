#! ruby -Ku
# -*- coding: utf-8 -*-
require "webrick"
config = {
    :Port => 3033,
    :DocumentRoot => '.'
}

WEBrick::HTTPServlet::FileHandler.add_handler("cgi", WEBrick::HTTPServlet::CGIHandler)
s = WEBrick::HTTPServer.new(config)

trap(:INT){
    s.shutdown
}
s.start