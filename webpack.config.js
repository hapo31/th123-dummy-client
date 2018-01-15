const { HotModuleReplacementPlugin } = require('webpack');
const path = require('path');

module.exports = {
    entry: "./web/src/index.tsx",
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "index.js",
        publicPath: "dist"
    },
    devServer: {
        contentBase: path.resolve(__dirname, "web")
    },
    devtool: "source-map",
    module: {
        loaders: [
            {
                loader: "ts-loader", // 読み込んだファイルを渡すプラグイン名
                test: /\.tsx?$/,  // 読み込むファイルのマッチ条件。
            },
            {
                loader: "file-loader",
                test: /.*\.html/,
            }
        ]
    },

    plugins: [
        new HotModuleReplacementPlugin()
    ]
};