module.exports = {
    mode: 'development',
    entry: {
      page1: './video_service/static/js/index.js',
      page2: './video_service/static/js/app.js',
      page3: './video_service/static/js/uicard.js',
    },
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
        {
          test: /\.js$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react']
            },
          },
        },
        
      ],
    }
  }