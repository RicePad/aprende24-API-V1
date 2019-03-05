module.exports = {
    mode: 'development',
    entry: './video_service/static/js/index.js',
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
      ],
    }
  }