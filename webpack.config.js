const path = require('path');

module.exports = {
  // path to our input file
  entry: {
    index: './src/assets/js/react/index.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { 
          presets: 
          ["@babel/preset-env", "@babel/preset-react"] 
        }
      },
      {
        test: /\.scss$/,
        include:  path.join(__dirname, './src/assets/styles/sass'),
        use:
        [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'sass-loader'
          },
        ]
      }
    ]
  },
  output: {
    // path to our Django static directory
    path: path.resolve(__dirname, './src/assets'),
    // output bundle file name
    filename: './js/[name]-bundle.js',
  },
  mode: "development"
};