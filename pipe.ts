// writeToPipe.ts
import * as fs from 'fs'
import * as path from 'path'

// 确定管道的路径
const pipePath = path.resolve('/tmp/pipe_demo');

// 要写入管道的信息
const infoMessage = "Hello, this is some info from TypeScript.\n";

// 使用fs模块向管道写入数据
fs.writeFile(pipePath, infoMessage, (err) => {
    if (err) {
        return console.error("Error writing to pipe:", err);
    }
    console.log("Message written to pipe successfully.");
});

