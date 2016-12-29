const webpack = require('webpack');
const ForceCaseSensitivityPlugin = require('case-sensitive-paths-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const baseConfig = require('./webpack.base.config.js');


module.exports = (opts) => {

  const config = baseConfig(opts);

  return {
    ...config,
    output: {
      ...config.output,
      publicPath: 'http://0.0.0.0:3000/bundles/',
    },
    plugins: [
      ...config.plugins,
      // local bundle stats file
      new BundleTracker({ filename: './webpack-stats.json' }),
      new webpack.NamedModulesPlugin(),
      new ForceCaseSensitivityPlugin(),  // OSX wont check but other unix os will
      new webpack.NoErrorsPlugin(),
    ],
  };
};
