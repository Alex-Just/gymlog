const path = require('path');
const webpack = require('webpack');

module.exports = (opts) => {

  const { PROJECT_ROOT, NODE_ENV } = opts;

  let plugins = [
    // add all common plugins here
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify(NODE_ENV),
      },
    }),
    // Promise and fetch polyfills
    new webpack.ProvidePlugin({
      Promise: 'imports-loader?this=>global!exports-loader?global.Promise!es6-promise',
    }),
  ];

  if (NODE_ENV !== 'test') {

    // karma webpack can't use these
    plugins = [
      ...plugins,

      // vendor chuncks
      new webpack.optimize.CommonsChunkPlugin({
        name: 'vendor',
        minChunks: function(module) {
          const userRequest = module.userRequest;

          if (typeof userRequest !== 'string') {
            return false;
          }

          // You can perform other similar checks here too.
          // Now we check just node_modules.
          return userRequest.indexOf('node_modules') >= 0;
        },

        filename: 'vendor-[hash].js',
      }),

      // shared stuff between chuncks
      new webpack.optimize.CommonsChunkPlugin({
        name: 'common',
        minChunks: Infinity,
        filename: 'common-[hash].js',
        chunks: [],  // add common modules here
      }),
    ];
  }

  return {
    context: PROJECT_ROOT,

    entry: {
      main: [
        'react-hot-loader/patch',
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        path.resolve(PROJECT_ROOT, 'src/index'),
      ],
      vendor: [
        'react-hot-loader/patch',
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        'react',
        'react-dom',
        'react-redux',
        'react-router',
        'redux',
      ],
    },

    output: {
      path: path.resolve(PROJECT_ROOT, 'src/bundles'),
      filename: '[name]-[hash].js',
    },

    plugins,

    module: {
      loaders: [
        {
          test: /\.jsx?$/,
          include: path.resolve(PROJECT_ROOT, 'src'),
          loaders: [
            'babel-loader',
          ],
        },

        // TODO: Hot reload doesn't work for global style.css
        {
          test: /\.css$/,
          exclude: /node_modules/,
          loaders: [
            'style-loader?sourceMap',
            'css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]',
          ],
        },

        {
          test: /\.scss$/,
          exclude: /node_modules/,
          loaders: [
            'style-loader?sourceMap',
            'css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]',
            'resolve-url-loader',
            'sass-loader?sourceMap',
          ],
        },

        { test: /\.(png|jpg|gif)$/, loader: 'url-loader', query: { limit: 8192 } },  // inline base64 URLs <=8k

        { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader' },
      ], // add all common loaders here
    },

    resolve: {
      extensions: ['.js', '.jsx'],
      modules: [
        'node_modules',
      ],
    },

    performance: {
      hints: process.env.NODE_ENV === 'production' ? 'warning' : false,
    },

    devServer: {
      // Enable history API fallback so HTML5 History API based
      // routing works. This is a good default that will come
      // in handy in more complicated setups.
      historyApiFallback: true,

      // Unlike the cli flag, this doesn't set
      // HotModuleReplacementPlugin!
      hot: true,
      inline: true,

      // Display only errors to reduce the amount of output.
      stats: 'errors-only',

      // Parse host and port from env to allow customization.
      //
      // If you use Vagrant or Cloud9, set
      // host: options.host || '0.0.0.0';
      //
      // 0.0.0.0 is available to all network devices
      // unlike default `localhost`.
      host: '0.0.0.0', // Defaults to `localhost`
      port: 3000, // Defaults to 8080
    },
  };
};
