"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// writeToPipe.ts
var fs = require("fs");
var path = require("path");
// 确定管道的路径
var pipePath = path.resolve('/tmp/pipe_demo');
// 要写入管道的信息
var infoMessage = "Hello, this is some info from TypeScript.\n";
// 使用fs模块向管道写入数据
fs.writeFile(pipePath, infoMessage, function (err) {
    if (err) {
        return console.error("Error writing to pipe:", err);
    }
    console.log("Message written to pipe successfully.");
});
