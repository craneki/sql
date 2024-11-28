<!DOCTYPE html>
<!-- saved from url=(0118)http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb -->
<html lang="zh-cn"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>二元函数梯度下降 - Jupyter Notebook</title>
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    


<script type="text/javascript" src="./21大数据张兆鹤-二元函数梯度下降_files/MathJax.js.下载" charset="utf-8"></script>

<script type="text/javascript">
// MathJax disabled, set as null to distinguish from *missing* MathJax,
// where it will be undefined, and should prompt a dialog later.
window.mathjax_url = "/static/components/MathJax/MathJax.js";
</script>

<link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/bootstrap-tour.min.css" type="text/css">
<link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/codemirror.css">


    <link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/style.min.css" type="text/css">
    

<link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/override.css" type="text/css">
<link rel="stylesheet" href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb" id="kernel-css" type="text/css">


    <link rel="stylesheet" href="./21大数据张兆鹤-二元函数梯度下降_files/custom.css" type="text/css">
    <script src="./21大数据张兆鹤-二元函数梯度下降_files/promise.min.js.下载" type="text/javascript" charset="utf-8"></script>
    <script src="./21大数据张兆鹤-二元函数梯度下降_files/react.production.min.js.下载" type="text/javascript"></script>
    <script src="./21大数据张兆鹤-二元函数梯度下降_files/react-dom.production.min.js.下载" type="text/javascript"></script>
    <script src="./21大数据张兆鹤-二元函数梯度下降_files/index.js.下载" type="text/javascript"></script>
    <script src="./21大数据张兆鹤-二元函数梯度下降_files/require.js.下载" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20241128152421",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}, "Manually edit the JSON below to manipulate the metadata for this cell.": ["\u624b\u52a8\u7f16\u8f91\u4e0b\u9762\u7684 JSON \u4ee3\u7801\u6765\u4fee\u6539\u5757\u5143\u6570\u636e\u3002"], "Manually edit the JSON below to manipulate the metadata for this notebook.": ["\u624b\u52a8\u7f16\u8f91\u4e0b\u9762\u7684 JSON \u4ee3\u7801\u6765\u4fee\u6539\u7b14\u8bb0\u672c\u5143\u6570\u636e\u3002"], " We recommend putting custom metadata attributes in an appropriately named substructure, so they don't conflict with those of others.": ["\u6211\u4eec\u5efa\u8bae\u5c06\u81ea\u5b9a\u4e49\u7684\u5143\u6570\u636e\u5c5e\u6027\u653e\u5165\u9002\u5f53\u7684\u5b50\u7ed3\u6784\u4e2d\uff0c\u8fd9\u6837\u5c31\u4e0d\u4f1a\u4e0e\u5176\u4ed6\u7684\u5b50\u7ed3\u6784\u53d1\u751f\u51b2\u7a81\u3002"], "Edit the metadata": ["\u7f16\u8f91\u5143\u6570\u636e"], "Edit Notebook Metadata": ["\u7f16\u8f91\u7b14\u8bb0\u672c\u5143\u6570\u636e"], "Edit Cell Metadata": ["\u7f16\u8f91\u5757\u5143\u6570\u636e"], "Cancel": ["\u53d6\u6d88"], "Edit": ["\u7f16\u8f91"], "OK": ["\u786e\u5b9a"], "Apply": ["\u5e94\u7528"], "WARNING: Could not save invalid JSON.": ["\u8b66\u544a: \u4e0d\u80fd\u4fdd\u5b58\u65e0\u6548\u7684JSON\u3002"], "There are no attachments for this cell.": ["\u8fd9\u4e2a\u5757\u6ca1\u6709\u9644\u4ef6\u3002"], "Current cell attachments": ["\u5f53\u524d\u5757\u9644\u4ef6"], "Attachments": ["\u9644\u4ef6"], "Restore": ["\u91cd\u65b0\u4fdd\u5b58"], "Delete": ["\u5220\u9664"], "Edit attachments": ["\u7f16\u8f91\u9644\u4ef6"], "Edit Notebook Attachments": ["\u7f16\u8f91\u7b14\u8bb0\u672c\u9644\u4ef6"], "Edit Cell Attachments": ["\u7f16\u8f91\u5757\u9644\u4ef6"], "Select a file to insert.": ["\u9009\u62e9\u6587\u4ef6\u63d2\u5165"], "Select a file": ["\u9009\u62e9\u6587\u4ef6"], "You are using Jupyter notebook.": ["\u60a8\u6b63\u5728\u4f7f\u7528 Jupyter Notebook\u3002"], "The version of the notebook server is: ": ["\u8be5 notebook \u670d\u52a1\u7684\u7248\u672c\u662f\uff1a"], "The server is running on this version of Python:": ["\u8be5\u670d\u52a1\u8fd0\u884c\u4e2d\u4f7f\u7528\u7684 Python \u7248\u672c\u4e3a:"], "Waiting for kernel to be available...": ["\u7b49\u5f85\u5185\u6838\u53ef\u7528..."], "Server Information:": ["\u670d\u52a1\u4fe1\u606f:"], "Current Kernel Information:": ["\u5f53\u524d\u5185\u6838\u4fe1\u606f:"], "Could not access sys_info variable for version information.": ["\u65e0\u6cd5\u8bbf\u95ee sys_info \u53d8\u91cf\u6765\u83b7\u53d6\u7248\u672c\u4fe1\u606f\u3002"], "Cannot find sys_info!": ["\u627e\u4e0d\u5230 sys_info\uff01"], "About Jupyter Notebook": ["\u5173\u4e8e Jupyter Notebook"], "unable to contact kernel": ["\u4e0d\u80fd\u8fde\u63a5\u5230\u5185\u6838"], "toggle rtl layout": ["\u5207\u6362 RTL \u5e03\u5c40"], "Toggle the screen directionality between left-to-right and right-to-left": ["\u5207\u6362\u5de6\u81f3\u53f3\u6216\u53f3\u81f3\u5de6\u7684\u5c4f\u5e55\u65b9\u5411"], "edit command mode keyboard shortcuts": ["\u7f16\u8f91\u547d\u4ee4\u6a21\u5f0f\u952e\u76d8\u5feb\u6377\u952e"], "Open a dialog to edit the command mode keyboard shortcuts": ["\u6253\u5f00\u7a97\u53e3\u6765\u7f16\u8f91\u5feb\u6377\u952e"], "restart kernel": ["\u91cd\u542f\u5185\u6838"], "restart the kernel (no confirmation dialog)": ["\u91cd\u542f\u5185\u6838\uff08\u65e0\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "confirm restart kernel": ["\u786e\u5b9a\u91cd\u542f\u5185\u6838"], "restart the kernel (with dialog)": ["\u91cd\u542f\u5185\u6838\uff08\u5e26\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "restart kernel and run all cells": ["\u91cd\u542f\u5185\u6838\u5e76\u4e14\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "restart the kernel, then re-run the whole notebook (no confirmation dialog)": ["\u91cd\u542f\u670d\u52a1\uff0c\u7136\u540e\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u7b14\u8bb0\u672c\uff08\u65e0\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "confirm restart kernel and run all cells": ["\u786e\u8ba4\u91cd\u542f\u5185\u6838\u5e76\u4e14\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "restart the kernel, then re-run the whole notebook (with dialog)": ["\u91cd\u542f\u5185\u6838, \u7136\u540e\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u4ee3\u7801\uff08\u5e26\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "restart kernel and clear output": ["\u91cd\u542f\u5185\u6838\u5e76\u4e14\u6e05\u7a7a\u8f93\u51fa"], "restart the kernel and clear all output (no confirmation dialog)": ["\u91cd\u542f\u5185\u6838\u5e76\u4e14\u6e05\u7a7a\u6240\u6709\u8f93\u51fa\uff08\u65e0\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "confirm restart kernel and clear output": ["\u786e\u8ba4\u91cd\u542f\u5185\u6838\u5e76\u4e14\u6e05\u7a7a\u8f93\u51fa"], "restart the kernel and clear all output (with dialog)": ["\u91cd\u542f\u5185\u6838\u5e76\u4e14\u6e05\u7a7a\u6240\u6709\u8f93\u51fa\uff08\u5e26\u786e\u8ba4\u5bf9\u8bdd\u6846\uff09"], "interrupt the kernel": ["\u4e2d\u65ad\u5185\u6838"], "run cell and select next": ["\u8fd0\u884c\u4ee3\u7801\u5757\u5e76\u4e14\u9009\u62e9\u4e0b\u4e00\u4e2a\u4ee3\u7801\u5757"], "run cell, select below": ["\u8fd0\u884c\u4ee3\u7801\u5757, \u9009\u62e9\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "run selected cells": ["\u8fd0\u884c\u9009\u4e2d\u7684\u4ee3\u7801\u5757"], "run cell and insert below": ["\u8fd0\u884c\u4ee3\u7801\u5757\u5e76\u4e14\u5728\u4e0b\u9762\u63d2\u5165\u4ee3\u7801\u5757"], "run all cells": ["\u8fd0\u884c\u6240\u6709\u7684\u4ee3\u7801\u5757"], "run all cells above": ["\u8fd0\u884c\u4e0a\u9762\u6240\u6709\u7684\u4ee3\u7801\u5757"], "run all cells below": ["\u8fd0\u884c\u4e0b\u9762\u6240\u6709\u7684\u4ee3\u7801\u5757"], "enter command mode": ["\u8fdb\u5165\u547d\u4ee4\u884c\u6a21\u5f0f"], "insert image": ["\u63d2\u5165\u56fe\u7247"], "cut cell attachments": ["\u526a\u5207\u4ee3\u7801\u5757\u7684\u9644\u4ef6"], "copy cell attachments": ["\u590d\u5236\u4ee3\u7801\u5757\u7684\u9644\u4ef6"], "paste cell attachments": ["\u7c98\u8d34\u4ee3\u7801\u5757\u7684\u9644\u4ef6"], "split cell at cursor": ["\u5728\u5149\u6807\u5904\u5206\u5272\u4ee3\u7801\u5757"], "enter edit mode": ["\u8fdb\u5165\u7f16\u8f91\u6a21\u5f0f"], "select previous cell": ["\u9009\u62e9\u4e0a\u4e00\u4e2a\u4ee3\u7801\u5757"], "select cell above": ["\u9009\u62e9\u4e0a\u9762\u7684\u4ee3\u7801\u5757"], "select next cell": ["\u9009\u62e9\u4e0b\u4e00\u4e2a\u4ee3\u7801\u5757"], "select cell below": ["\u9009\u62e9\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "extend selection above": ["\u6269\u5c55\u4e0a\u9762\u7684\u4ee3\u7801\u5757"], "extend selected cells above": ["\u6269\u5c55\u4e0a\u9762\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "extend selection below": ["\u6269\u5c55\u4e0b\u9762\u7684\u4ee3\u7801\u5757"], "extend selected cells below": ["\u6269\u5c55\u4e0b\u9762\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "cut selected cells": ["\u526a\u5207\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "copy selected cells": ["\u590d\u5236\u9009\u62e9\u7684\u4ee3\u7801\u5757"], "paste cells above": ["\u7c98\u8d34\u5230\u4e0a\u9762"], "paste cells below": ["\u7c98\u8d34\u5230\u4e0b\u9762"], "insert cell above": ["\u5728\u4e0a\u9762\u63d2\u5165\u4ee3\u7801\u5757"], "insert cell below": ["\u5728\u4e0b\u9762\u63d2\u5165\u4ee3\u7801\u5757"], "change cell to code": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u4ee3\u7801"], "change cell to markdown": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210 Markdown"], "change cell to raw": ["\u6e05\u9664\u4ee3\u7801\u5757\u683c\u5f0f"], "change cell to heading 1": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 1"], "change cell to heading 2": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 2"], "change cell to heading 3": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 3"], "change cell to heading 4": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 4"], "change cell to heading 5": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 5"], "change cell to heading 6": ["\u628a\u4ee3\u7801\u5757\u53d8\u6210\u6807\u9898 6"], "toggle cell output": ["\u5207\u6362\u4ee3\u7801\u5757\u8f93\u51fa"], "toggle output of selected cells": ["\u5207\u6362\u9009\u5b9a\u5355\u5143\u683c\u7684\u8f93\u51fa"], "toggle cell scrolling": ["\u5207\u6362\u5355\u5143\u683c\u6eda\u52a8"], "toggle output scrolling of selected cells": ["\u5207\u6362\u9009\u4e2d\u5355\u5143\u683c\u7684\u8f93\u51fa\u6eda\u52a8"], "clear cell output": ["\u6e05\u7a7a\u6240\u6709\u5355\u5143\u683c\u8f93\u51fa"], "clear output of selected cells": ["\u6e05\u7a7a\u5df2\u9009\u62e9\u5355\u5143\u683c\u7684\u8f93\u51fa"], "move cells down": ["\u4e0b\u79fb"], "move selected cells down": ["\u4e0b\u79fb\u9009\u4e2d\u5355\u5143\u683c"], "move cells up": ["\u4e0a\u79fb"], "move selected cells up": ["\u4e0a\u79fb\u9009\u4e2d\u5355\u5143\u683c"], "toggle line numbers": ["\u5207\u6362\u884c\u53f7"], "show keyboard shortcuts": ["\u663e\u793a\u952e\u76d8\u5feb\u6377\u952e"], "delete cells": ["\u5220\u9664\u5355\u5143\u683c"], "delete selected cells": ["\u5220\u9664\u9009\u4e2d\u5355\u5143\u683c"], "undo cell deletion": ["\u64a4\u9500\u5220\u9664"], "merge cell with previous cell": ["\u5408\u5e76\u4e0a\u4e00\u4e2a\u5355\u5143\u683c"], "merge cell above": ["\u5408\u5e76\u4e0a\u9762\u7684\u5355\u5143\u683c"], "merge cell with next cell": ["\u5408\u5e76\u4e0b\u4e00\u4e2a\u5355\u5143\u683c"], "merge cell below": ["\u5408\u5e76\u4e0b\u9762\u7684\u5355\u5143\u683c"], "merge selected cells": ["\u5408\u5e76\u9009\u4e2d\u7684\u5355\u5143\u683c"], "merge cells": ["\u5408\u5e76\u5355\u5143\u683c"], "merge selected cells, or current cell with cell below if only one cell is selected": ["\u5408\u5e76\u9009\u4e2d\u5355\u5143\u683c, \u5982\u679c\u53ea\u6709\u4e00\u4e2a\u5355\u5143\u683c\u88ab\u9009\u4e2d"], "show command pallette": ["\u663e\u793a\u547d\u4ee4\u914d\u7f6e"], "open the command palette": ["\u6253\u5f00\u547d\u4ee4\u914d\u7f6e"], "toggle all line numbers": ["\u5207\u6362\u6240\u6709\u884c\u53f7"], "toggles line numbers in all cells, and persist the setting": ["\u5728\u6240\u6709\u5355\u5143\u683c\u4e2d\u5207\u6362\u884c\u53f7\uff0c\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "show all line numbers": ["\u663e\u793a\u884c\u53f7"], "show line numbers in all cells, and persist the setting": ["\u5728\u6240\u6709\u5355\u5143\u683c\u4e2d\u663e\u793a\u884c\u53f7\uff0c\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "hide all line numbers": ["\u9690\u85cf\u884c\u53f7"], "hide line numbers in all cells, and persist the setting": ["\u9690\u85cf\u884c\u53f7\u5e76\u4fdd\u6301\u8bbe\u7f6e"], "toggle header": ["\u5207\u6362\u6807\u9898"], "switch between showing and hiding the header": ["\u5207\u6362\u663e\u793a\u548c\u9690\u85cf\u6807\u9898"], "show the header": ["\u663e\u793a\u6807\u9898"], "hide the header": ["\u9690\u85cf\u6807\u9898"], "toggle toolbar": ["\u5207\u6362\u5de5\u5177\u680f"], "switch between showing and hiding the toolbar": ["\u5207\u6362\u663e\u793a/\u9690\u85cf\u5de5\u5177\u680f"], "show the toolbar": ["\u663e\u793a\u5de5\u5177\u680f"], "hide the toolbar": ["\u9690\u85cf\u5de5\u5177\u680f"], "close the pager": ["\u5173\u95ed\u5206\u9875\u5668"], "ignore": ["\u5ffd\u7565"], "move cursor up": ["\u5149\u6807\u4e0a\u79fb"], "move cursor down": ["\u5149\u6807\u4e0b\u79fb"], "scroll notebook down": ["\u5411\u4e0b\u6eda\u52a8"], "scroll notebook up": ["\u5411\u4e0a\u6eda\u52a8"], "scroll cell center": ["\u6eda\u52a8\u5355\u5143\u683c\u5230\u4e2d\u95f4"], "Scroll the current cell to the center": ["\u628a\u5f53\u524d\u5355\u5143\u683c\u6eda\u52a8\u5230\u4e2d\u95f4"], "scroll cell top": ["\u6eda\u52a8\u5355\u5143\u683c\u5230\u9876"], "Scroll the current cell to the top": ["\u5c06\u5f53\u524d\u5355\u5143\u683c\u6eda\u52a8\u5230\u9876\u90e8"], "duplicate notebook": ["\u5236\u4f5c\u7b14\u8bb0\u672c\u526f\u672c"], "Create and open a copy of the current notebook": ["\u521b\u5efa\u5e76\u6253\u5f00\u5f53\u524d\u7b14\u8bb0\u672c\u7684\u4e00\u4e2a\u526f\u672c"], "trust notebook": ["\u4fe1\u4efb\u7b14\u8bb0\u672c"], "Trust the current notebook": ["\u4fe1\u4efb\u5f53\u524d\u7b14\u8bb0\u672c"], "rename notebook": ["\u91cd\u547d\u540d\u7b14\u8bb0\u672c"], "Rename the current notebook": ["\u91cd\u547d\u540d\u5f53\u524d\u7b14\u8bb0\u672c"], "toggle all cells output collapsed": ["\u5207\u6362\u6298\u53e0\u6240\u6709\u5355\u5143\u683c\u7684\u8f93\u51fa"], "Toggle the hidden state of all output areas": ["\u5207\u6362\u6240\u6709\u8f93\u51fa\u533a\u57df\u7684\u9690\u85cf\u72b6\u6001"], "toggle all cells output scrolled": ["\u5207\u6362\u6240\u6709\u5355\u5143\u683c\u8f93\u51fa\u7684\u6eda\u52a8\u72b6\u6001"], "Toggle the scrolling state of all output areas": ["\u5207\u6362\u6240\u6709\u8f93\u51fa\u533a\u57df\u7684\u6eda\u52a8\u72b6\u6001"], "clear all cells output": ["\u6e05\u7a7a\u6240\u6709\u5355\u5143\u683c\u8f93\u51fa"], "Clear the content of all the outputs": ["\u6e05\u7a7a\u6240\u6709\u7684\u8f93\u51fa\u5185\u5bb9"], "save notebook": ["\u4fdd\u5b58\u7b14\u8bb0\u672c"], "Save and Checkpoint": ["\u4fdd\u5b58\u5e76\u5efa\u7acb\u68c0\u67e5\u70b9"], "Warning: accessing Cell.cm_config directly is deprecated.": ["\u8b66\u544a: \u76f4\u63a5\u8bbf\u95ee Cell.cm_config \u5df2\u7ecf\u88ab\u5f03\u7528\u4e86\u3002"], "Unrecognized cell type: %s": ["\u672a\u77e5\u7684\u5355\u5143\u683c\u7c7b\u578b: %s"], "Unrecognized cell type": ["\u672a\u77e5\u7684\u5355\u5143\u683c\u7c7b\u578b"], "Error in cell toolbar callback %s": ["\u5de5\u5177\u680f\u8c03\u7528 %s \u51fa\u73b0\u9519\u8bef"], "Clipboard types: %s": ["\u526a\u8d34\u677f\u7c7b\u578b: %s"], "Dialog for paste from system clipboard": ["\u4ece\u7cfb\u7edf\u526a\u5207\u677f\u7c98\u8d34"], "Ctrl-V": [""], "Cmd-V": [""], "Press %s again to paste": ["\u518d\u6309\u4e00\u6b21 %s \u6765\u7c98\u8d34"], "Why is this needed? ": ["\u4e3a\u4ec0\u4e48\u9700\u8981\u5b83?"], "We can't get paste events in this browser without a text box. ": ["\u5728\u6d4f\u89c8\u5668\u91cc\u6ca1\u6709\u6587\u672c\u6846\u6211\u4eec\u4e0d\u80fd\u7c98\u8d34. "], "There's an invisible text box focused in this dialog.": ["\u5728\u8fd9\u4e2a\u5bf9\u8bdd\u6846\u4e2d\u6709\u4e00\u4e2a\u4e0d\u53ef\u89c1\u7684\u6587\u672c\u6846."], "%s to paste": ["%s \u6765\u7c98\u8d34"], "Can't execute cell since kernel is not set.": ["\u5f53\u524d\u4e0d\u80fd\u6267\u884c\u5355\u5143\u683c\u4ee3\u7801\uff0c\u56e0\u4e3a\u5185\u6838\u8fd8\u6ca1\u6709\u51c6\u5907\u597d\u3002"], "In": [""], "Could not find a kernel matching %s. Please select a kernel:": ["\u627e\u4e0d\u5230\u5339\u914d %s \u7684\u5185\u6838\u3002\u8bf7\u9009\u62e9\u4e00\u4e2a\u5185\u6838:"], "Continue Without Kernel": ["\u65e0\u5185\u6838\u7ee7\u7eed\u8fd0\u884c"], "Set Kernel": ["\u8bbe\u7f6e\u5185\u6838"], "Kernel not found": ["\u627e\u4e0d\u5230\u5185\u6838"], "Creating Notebook Failed": ["\u521b\u5efa\u7b14\u8bb0\u672c\u5931\u8d25"], "The error was: %s": ["\u9519\u8bef\uff1a %s"], "Run": ["\u8fd0\u884c"], "Code": ["\u4ee3\u7801"], "Markdown": ["Markdown"], "Raw NBConvert": ["\u539f\u751f NBConvert"], "Heading": ["\u6807\u9898"], "unrecognized cell type:": ["\u672a\u8bc6\u522b\u7684\u5355\u5143\u683c\u7c7b\u578b\uff1a"], "Failed to retrieve MathJax from '%s'": ["\u672a\u80fd\u4ece '%s' \u4e2d\u68c0\u7d22 MathJax"], "Math/LaTeX rendering will be disabled.": ["Math/LaTeX \u6e32\u67d3\u5c06\u88ab\u7981\u7528\u3002"], "Trusted Notebook": ["\u53ef\u4fe1\u7684\u7b14\u8bb0\u672c"], "Trust Notebook": ["\u4fe1\u4efb\u7b14\u8bb0\u672c"], "None": ["\u65e0"], "No checkpoints": ["\u6ca1\u6709\u68c0\u67e5\u70b9"], "Opens in a new window": ["\u5728\u65b0\u7a97\u53e3\u6253\u5f00"], "Autosave in progress, latest changes may be lost.": ["\u81ea\u52a8\u4fdd\u5b58\u8fdb\u884c\u4e2d\uff0c\u6700\u65b0\u7684\u6539\u53d8\u53ef\u80fd\u4f1a\u4e22\u5931\u3002"], "Unsaved changes will be lost.": ["\u672a\u4fdd\u5b58\u7684\u4fee\u6539\u5c06\u4f1a\u4e22\u5931\u3002"], "The Kernel is busy, outputs may be lost.": ["\u5185\u6838\u6b63\u5fd9\uff0c\u8f93\u51fa\u4e5f\u8bb8\u4f1a\u4e22\u5931\u3002"], "This notebook is version %1$s, but we only fully support up to %2$s.": ["\u8be5\u7b14\u8bb0\u672c\u4f7f\u7528\u4e86\u7248\u672c %1$s\uff0c\u4f46\u662f\u6211\u4eec\u53ea\u652f\u6301\u5230 %2$s."], "You can still work with this notebook, but cell and output types introduced in later notebook versions will not be available.": ["\u60a8\u4ecd\u7136\u53ef\u4ee5\u4f7f\u7528\u8be5\u7b14\u8bb0\u672c\uff0c\u4f46\u662f\u5728\u65b0\u7248\u672c\u4e2d\u5f15\u5165\u7684\u5355\u5143\u548c\u8f93\u51fa\u7c7b\u578b\u5c06\u4e0d\u53ef\u7528\u3002"], "Restart and Run All Cells": ["\u91cd\u542f\u5e76\u8fd0\u884c\u6240\u6709\u4ee3\u7801\u5757"], "Restart and Clear All Outputs": ["\u91cd\u542f\u5e76\u6e05\u7a7a\u6240\u6709\u8f93\u51fa"], "Restart": ["\u91cd\u542f"], "Continue Running": ["\u7ee7\u7eed\u8fd0\u884c"], "Reload": ["\u91cd\u8f7d"], "Overwrite": ["\u91cd\u5199"], "Trust": ["\u4fe1\u4efb"], "Revert": ["\u6062\u590d"], "Newer Notebook": ["\u65b0\u7b14\u8bb0\u672c"], "Use markdown headings": ["\u4f7f\u7528 Markdown \u6807\u9898"], "Jupyter no longer uses special heading cells. Instead, write your headings in Markdown cells using # characters:": ["Jupyter \u4e0d\u518d\u4f7f\u7528\u7279\u6b8a\u7684\u6807\u9898\u5355\u5143\u683c\u3002\u8bf7\u5728 Markdown \u5355\u5143\u683c\u4e2d\u4f7f\u7528 # \u5b57\u7b26\u6765\u5199\u6807\u9898\uff1a"], "## This is a level 2 heading": ["## \u8fd9\u662f\u4e00\u4e2a\u4e8c\u7ea7\u6807\u9898"], "Restart kernel and re-run the whole notebook?": ["\u91cd\u65b0\u542f\u52a8\u5185\u6838\u5e76\u91cd\u65b0\u8fd0\u884c\u6574\u4e2a\u7b14\u8bb0\u672c\uff1f"], "Are you sure you want to restart the current kernel and re-execute the whole notebook?  All variables and outputs will be lost.": ["\u60a8\u786e\u5b9a\u8981\u91cd\u65b0\u542f\u52a8\u5f53\u524d\u7684\u5185\u6838\u5e76\u91cd\u65b0\u6267\u884c\u6574\u4e2a\u7b14\u8bb0\u672c\u5417\uff1f\u6240\u6709\u7684\u53d8\u91cf\u548c\u8f93\u51fa\u90fd\u5c06\u4e22\u5931\u3002"], "Restart kernel and clear all output?": ["\u91cd\u542f\u5185\u6838\u5e76\u4e14\u6e05\u7a7a\u8f93\u51fa\uff1f"], "Do you want to restart the current kernel and clear all output?  All variables and outputs will be lost.": ["\u60a8\u662f\u5426\u5e0c\u671b\u91cd\u65b0\u542f\u52a8\u5f53\u524d\u7684\u5185\u6838\u5e76\u6e05\u9664\u6240\u6709\u8f93\u51fa\uff1f\u6240\u6709\u7684\u53d8\u91cf\u548c\u8f93\u51fa\u90fd\u5c06\u4e22\u5931\u3002"], "Restart kernel?": ["\u91cd\u542f\u5185\u6838\uff1f"], "Do you want to restart the current kernel?  All variables will be lost.": ["\u5982\u679c\u91cd\u542f\u5185\u6838\uff0c\u6240\u6709\u53d8\u91cf\u90fd\u4f1a\u4e22\u5931\u3002\u662f\u5426\u91cd\u542f\uff1f"], "Shutdown kernel?": ["\u5173\u95ed\u5185\u6838\uff1f"], "Do you want to shutdown the current kernel?  All variables will be lost.": ["\u5982\u679c\u5173\u95ed\u5185\u6838\uff0c\u6240\u6709\u53d8\u91cf\u90fd\u4f1a\u4e22\u5931\u3002\u662f\u5426\u5173\u95ed\uff1f"], "Notebook changed": ["\u7b14\u8bb0\u672c\u6539\u53d8\u4e86"], "The notebook file has changed on disk since the last time we opened or saved it. Do you want to overwrite the file on disk with the version open here, or load the version on disk (reload the page)?": ["\u81ea\u4ece\u4e0a\u6b21\u6211\u4eec\u6253\u5f00\u6216\u4fdd\u5b58\u5b83\u4ee5\u6765\uff0c\u7b14\u8bb0\u672c\u6587\u4ef6\u5df2\u7ecf\u5728\u78c1\u76d8\u4e0a\u53d1\u751f\u4e86\u53d8\u5316\u3002\u60a8\u5e0c\u671b\u7528\u8fd9\u91cc\u6253\u5f00\u7684\u7248\u672c\u8986\u76d6\u78c1\u76d8\u4e0a\u7684\u7248\u672c\uff0c\u8fd8\u662f\u52a0\u8f7d\u78c1\u76d8\u4e0a\u7684\u7248\u672c\uff08\u5237\u65b0\u9875\u9762\uff09\uff1f"], "Notebook validation failed": ["Notebook \u6821\u9a8c\u5931\u8d25"], "The save operation succeeded, but the notebook does not appear to be valid. The validation error was:": ["\u4fdd\u5b58\u64cd\u4f5c\u6210\u529f\u4e86\uff0c\u4f46\u662f\u8fd9\u4e2a\u7b14\u8bb0\u672c\u770b\u8d77\u6765\u5e76\u4e0d\u6709\u6548\u3002\u6821\u9a8c\u9519\u8bef\uff1a"], "A trusted Jupyter notebook may execute hidden malicious code when you open it. Selecting trust will immediately reload this notebook in a trusted state. For more information, see the Jupyter security documentation: ": ["\u5f53\u4f60\u6253\u5f00\u4e00\u4e2a\u53ef\u4fe1\u4efb\u7684 Jupyter \u7b14\u8bb0\u672c\u65f6\uff0c\u5b83\u53ef\u80fd\u4f1a\u6267\u884c\u9690\u85cf\u7684\u6076\u610f\u4ee3\u7801\u3002\u9009\u62e9\u4fe1\u4efb\u5c06\u7acb\u5373\u5728\u4e00\u4e2a\u53ef\u4fe1\u7684\u72b6\u6001\u4e2d\u91cd\u65b0\u52a0\u8f7d\u8fd9\u4e2a\u7b14\u8bb0\u672c\u3002\u8981\u4e86\u89e3\u66f4\u591a\u4fe1\u606f\uff0c\u8bf7\u53c2\u9605 Jupyter \u5b89\u5168\u6587\u6863\uff1a"], "here": ["\u8fd9\u91cc"], "Trust this notebook?": ["\u4fe1\u4efb\u8fd9\u4e2a\u7b14\u8bb0\u672c\uff1f"], "Notebook failed to load": ["\u7b14\u8bb0\u672c\u52a0\u8f7d\u5931\u8d25"], "The error was: ": ["\u9519\u8bef: "], "See the error console for details.": ["\u6709\u5173\u8be6\u7ec6\u4fe1\u606f\uff0c\u8bf7\u53c2\u9605\u9519\u8bef\u63a7\u5236\u53f0\u3002"], "The notebook also failed validation:": ["\u8fd9\u4e2a\u7b14\u8bb0\u672c\u6821\u9a8c\u4e5f\u5931\u8d25\u4e86:"], "An invalid notebook may not function properly. The validation error was:": ["\u65e0\u6548\u7684\u7b14\u8bb0\u672c\u53ef\u80fd\u65e0\u6cd5\u6b63\u5e38\u8fd0\u884c\u3002\u6821\u9a8c\u9519\u8bef\uff1a"], "This notebook has been converted from an older notebook format to the current notebook format v(%s).": ["\u672c\u7b14\u8bb0\u672c\u5df2\u4ece\u8f83\u65e7\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u8f6c\u6362\u4e3a\u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f v(%s)\u3002"], "This notebook has been converted from a newer notebook format to the current notebook format v(%s).": ["\u8fd9\u4e2a\u7b14\u8bb0\u672c\u5df2\u7ecf\u4ece\u4e00\u79cd\u65b0\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u8f6c\u6362\u4e3a\u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f v(%s)\u3002"], "The next time you save this notebook, the current notebook format will be used.": ["\u4e0b\u6b21\u4f60\u4fdd\u5b58\u8fd9\u4e2a\u7b14\u8bb0\u672c\u65f6\uff0c\u5f53\u524d\u7684\u7b14\u8bb0\u672c\u683c\u5f0f\u5c06\u4f1a\u88ab\u4f7f\u7528\u3002"], "Older versions of Jupyter may not be able to read the new format.": ["\u65e7\u7248\u672c\u7684 Jupyter \u53ef\u80fd\u65e0\u6cd5\u8bfb\u53d6\u65b0\u683c\u5f0f\u3002"], "Some features of the original notebook may not be available.": ["\u539f\u7b14\u8bb0\u672c\u7684\u4e00\u4e9b\u7279\u6027\u53ef\u80fd\u65e0\u6cd5\u4f7f\u7528\u3002"], "To preserve the original version, close the notebook without saving it.": ["\u4e3a\u4e86\u4fdd\u5b58\u539f\u59cb\u7248\u672c\uff0c\u5173\u95ed\u7b14\u8bb0\u672c\u800c\u4e0d\u4fdd\u5b58\u5b83\u3002"], "Notebook converted": ["\u5df2\u8f6c\u6362\u7b14\u8bb0\u672c"], "(No name)": ["\uff08\u6ca1\u6709\u540d\u5b57\uff09"], "An unknown error occurred while loading this notebook. This version can load notebook formats %s or earlier. See the server log for details.": ["\u52a0\u8f7d\u672c\u7b14\u8bb0\u672c\u65f6\u51fa\u73b0\u4e86\u4e00\u4e2a\u672a\u77e5\u7684\u9519\u8bef\u3002\u8fd9\u4e2a\u7248\u672c\u53ef\u4ee5\u52a0\u8f7d %s \u6216\u66f4\u65e9\u7684\u7b14\u8bb0\u672c\u3002\u6709\u5173\u8be6\u7ec6\u4fe1\u606f\uff0c\u8bf7\u53c2\u9605\u670d\u52a1\u5668\u65e5\u5fd7\u3002"], "Error loading notebook": ["\u52a0\u8f7d\u7b14\u8bb0\u672c\u51fa\u9519"], "Are you sure you want to revert the notebook to the latest checkpoint?": ["\u786e\u5b9a\u5c06\u7b14\u8bb0\u672c\u6062\u590d\u81f3\u6700\u8fd1\u7684\u68c0\u67e5\u70b9\uff1f"], "This cannot be undone.": ["\u8be5\u64cd\u4f5c\u4e0d\u80fd\u88ab\u8fd8\u539f\u3002"], "The checkpoint was last updated at:": ["\u7b14\u8bb0\u672c\u7684\u6700\u65b0\u68c0\u67e5\u70b9\u66f4\u65b0\u4e8e\uff1a"], "Revert notebook to checkpoint": ["\u6062\u590d\u7b14\u8bb0\u672c\u81f3\u68c0\u67e5\u70b9"], "Edit Mode": ["\u7f16\u8f91\u6a21\u5f0f"], "Command Mode": ["\u547d\u4ee4\u6a21\u5f0f"], "Kernel Created": ["\u5185\u6838\u5df2\u521b\u5efa"], "Connecting to kernel": ["\u6b63\u5728\u8fde\u63a5\u5185\u6838"], "Not Connected": ["\u672a\u8fde\u63a5"], "click to reconnect": ["\u70b9\u51fb\u91cd\u8fde"], "Restarting kernel": ["\u91cd\u542f\u5185\u6838"], "Kernel Restarting": ["\u5185\u6838\u6b63\u5728\u91cd\u542f"], "The kernel appears to have died. It will restart automatically.": ["\u5185\u6838\u4f3c\u4e4e\u6302\u6389\u4e86\uff0c\u5b83\u5f88\u5feb\u5c06\u81ea\u52a8\u91cd\u542f\u3002"], "Dead kernel": ["\u6302\u6389\u7684\u5185\u6838"], "Kernel Dead": ["\u5185\u6838\u6302\u6389"], "Interrupting kernel": ["\u6b63\u5728\u4e2d\u65ad\u5185\u6838"], "No Connection to Kernel": ["\u6ca1\u6709\u8fde\u63a5\u5230\u5185\u6838"], "A connection to the notebook server could not be established. The notebook will continue trying to reconnect. Check your network connection or notebook server configuration.": ["\u65e0\u6cd5\u5efa\u7acb\u5230\u7b14\u8bb0\u672c\u670d\u52a1\u5668\u7684\u8fde\u63a5\u3002 \u6211\u4eec\u4f1a\u7ee7\u7eed\u5c1d\u8bd5\u91cd\u8fde\u3002\u8bf7\u68c0\u67e5\u7f51\u7edc\u8fde\u63a5\u8fd8\u6709\u670d\u52a1\u914d\u7f6e\u3002"], "Connection failed": ["\u8fde\u63a5\u5931\u8d25"], "No kernel": ["\u6ca1\u6709\u5185\u6838"], "Kernel is not running": ["\u5185\u6838\u6ca1\u6709\u8fd0\u884c"], "Don't Restart": ["\u4e0d\u8981\u91cd\u542f"], "Try Restarting Now": ["\u73b0\u5728\u5c1d\u8bd5\u91cd\u542f"], "The kernel has died, and the automatic restart has failed. It is possible the kernel cannot be restarted. If you are not able to restart the kernel, you will still be able to save the notebook, but running code will no longer work until the notebook is reopened.": ["\u5185\u6838\u5df2\u7ecf\u6b7b\u4ea1\uff0c\u81ea\u52a8\u91cd\u542f\u4e5f\u5931\u8d25\u4e86\u3002\u53ef\u80fd\u662f\u5185\u6838\u4e0d\u80fd\u91cd\u65b0\u542f\u52a8\u3002\u5982\u679c\u60a8\u4e0d\u80fd\u91cd\u65b0\u542f\u52a8\u5185\u6838\uff0c\u60a8\u4ecd\u7136\u80fd\u591f\u4fdd\u5b58\u7b14\u8bb0\u672c\uff0c\u4f46\u7b14\u8bb0\u672c\u8981\u91cd\u65b0\u6253\u5f00\u624d\u80fd\u8fd0\u884c\u4ee3\u7801\u3002"], "No Kernel": ["\u6ca1\u6709\u5185\u6838"], "Failed to start the kernel": ["\u542f\u52a8\u5185\u6838\u5931\u8d25"], "Kernel Busy": ["\u5185\u6838\u6b63\u5fd9"], "Kernel starting, please wait...": ["\u5185\u6838\u6b63\u5728\u542f\u52a8,\u8bf7\u7b49\u5f85..."], "Kernel Idle": ["\u5185\u6838\u7a7a\u95f2"], "Kernel ready": ["\u5185\u6838\u5c31\u7eea"], "Using kernel: ": ["\u4f7f\u7528\u5185\u6838\uff1a"], "Only candidate for language: %1$s was %2$s.": ["\u53ea\u652f\u6301\u8bed\u8a00\uff1a %1$s - %2$s."], "Loading notebook": ["\u52a0\u8f7d\u7b14\u8bb0\u672c"], "Notebook loaded": ["\u7b14\u8bb0\u672c\u5df2\u52a0\u8f7d"], "Saving notebook": ["\u4fdd\u5b58\u7b14\u8bb0\u672c"], "Notebook saved": ["\u7b14\u8bb0\u672c\u5df2\u4fdd\u5b58"], "Notebook save failed": ["\u7b14\u8bb0\u672c\u4fdd\u5b58\u5931\u8d25"], "Notebook copy failed": ["\u7b14\u8bb0\u672c\u590d\u5236\u5931\u8d25"], "Checkpoint created": ["\u68c0\u67e5\u70b9\u5df2\u521b\u5efa"], "Checkpoint failed": ["\u68c0\u67e5\u70b9\u521b\u5efa\u5931\u8d25"], "Checkpoint deleted": ["\u68c0\u67e5\u70b9\u5df2\u5220\u9664"], "Checkpoint delete failed": ["\u68c0\u67e5\u70b9\u5220\u9664\u5931\u8d25"], "Restoring to checkpoint...": ["\u6b63\u5728\u6062\u590d\u81f3\u68c0\u67e5\u70b9..."], "Checkpoint restore failed": ["\u68c0\u67e5\u70b9\u6062\u590d\u5931\u8d25"], "Autosave disabled": ["\u81ea\u52a8\u4fdd\u5b58\u5931\u8d25"], "Saving every %d sec.": ["\u6bcf\u9694 %s \u79d2\u4fdd\u5b58\u4e00\u6b21\u3002"], "Trusted": ["\u53ef\u4fe1"], "Not Trusted": ["\u4e0d\u53ef\u4fe1"], "click to expand output": ["\u70b9\u51fb\u5c55\u5f00\u8f93\u51fa"], "click to expand output; double click to hide output": ["\u70b9\u51fb\u5c55\u5f00\u8f93\u51fa\uff1b\u53cc\u51fb\u9690\u85cf\u8f93\u51fa"], "click to unscroll output; double click to hide": ["\u5355\u51fb\u53d6\u6d88\u6eda\u52a8\u8f93\u51fa\uff1b\u53cc\u51fb\u9690\u85cf"], "click to scroll output; double click to hide": ["\u70b9\u51fb\u6eda\u52a8\u8f93\u51fa\uff1b\u53cc\u51fb\u9690\u85cf"], "Javascript error adding output!": ["\u6dfb\u52a0\u8f93\u51fa\u65f6 Javascript \u51fa\u9519\u4e86\uff01"], "See your browser Javascript console for more details.": ["\u66f4\u591a\u7ec6\u8282\u8bf7\u53c2\u89c1\u60a8\u7684\u6d4f\u89c8\u5668 Javascript \u63a7\u5236\u53f0\u3002"], "Out[%d]:": [""], "Unrecognized output: %s": ["\u672a\u8bc6\u522b\u7684\u8f93\u51fa\uff1a %s"], "Open the pager in an external window": ["\u5728\u5916\u90e8\u7a97\u53e3\u6253\u5f00\u5206\u9875\u5668"], "Close the pager": ["\u5173\u95ed\u5206\u9875\u5668"], "Jupyter Pager": ["Jupyter \u5206\u9875\u5668"], "go to cell start": ["\u8df3\u5230\u5355\u5143\u683c\u8d77\u59cb\u5904"], "go to cell end": ["\u8df3\u5230\u5355\u5143\u683c\u6700\u540e"], "go one word left": ["\u5f80\u5de6\u8df3\u4e00\u4e2a\u5355\u8bcd"], "go one word right": ["\u5f80\u53f3\u8df3\u4e00\u4e2a\u5355\u8bcd"], "delete word before": ["\u5220\u9664\u524d\u9762\u7684\u5355\u8bcd"], "delete word after": ["\u5220\u9664\u540e\u9762\u7684\u5355\u8bcd"], "redo": ["\u91cd\u505a"], "redo selection": ["\u91cd\u65b0\u9009\u62e9"], "emacs-style line kill": ["Emacs \u98ce\u683c\u7684 Line Kill"], "delete line left of cursor": ["\u5220\u9664\u5149\u6807\u5de6\u8fb9\u4e00\u884c"], "delete line right of cursor": ["\u5220\u9664\u5149\u6807\u53f3\u8fb9\u4e00\u884c"], "code completion or indent": ["\u4ee3\u7801\u8865\u5168\u6216\u7f29\u8fdb"], "tooltip": ["\u5de5\u5177\u63d0\u793a"], "indent": ["\u7f29\u8fdb"], "dedent": ["\u53d6\u6d88\u7f29\u8fdb"], "select all": ["\u5168\u9009"], "undo": ["\u64a4\u9500"], "comment": ["\u6ce8\u91ca"], "delete whole line": ["\u5220\u9664\u6574\u884c"], "undo selection": ["\u64a4\u9500\u9009\u62e9"], "toggle overwrite flag": ["\u5207\u6362\u91cd\u5199\u6807\u5fd7"], "Shift": ["Shift"], "Alt": ["Alt"], "Up": ["\u4e0a"], "Down": ["\u4e0b"], "Left": ["\u5de6"], "Right": ["\u53f3"], "Tab": ["Tab"], "Caps Lock": ["\u5927\u5199\u9501\u5b9a"], "Esc": ["Esc"], "Ctrl": ["Ctrl"], "Enter": ["Enter"], "Page Up": ["\u4e0a\u4e00\u9875"], "Page Down": ["\u4e0b\u4e00\u9875"], "Home": ["Home"], "End": ["End"], "Space": ["\u7a7a\u683c"], "Backspace": ["\u9000\u683c"], "Minus": [""], "PageUp": ["\u4e0a\u4e00\u9875"], "The Jupyter Notebook has two different keyboard input modes.": ["Jupyter \u7b14\u8bb0\u672c\u6709\u4e24\u79cd\u4e0d\u540c\u7684\u952e\u76d8\u8f93\u5165\u6a21\u5f0f\u3002"], "<b>Edit mode</b> allows you to type code or text into a cell and is indicated by a green cell border.": ["<b>\u7f16\u8f91\u6a21\u5f0f</b>\u5141\u8bb8\u60a8\u5c06\u4ee3\u7801\u6216\u6587\u672c\u8f93\u5165\u5230\u4e00\u4e2a\u5355\u5143\u683c\u4e2d\uff0c\u5e76\u901a\u8fc7\u4e00\u4e2a\u7eff\u8272\u8fb9\u6846\u7684\u5355\u5143\u683c\u6765\u8868\u793a"], "<b>Command mode</b> binds the keyboard to notebook level commands and is indicated by a grey cell border with a blue left margin.": ["<b>\u547d\u4ee4\u6a21\u5f0f</b>\u5c06\u952e\u76d8\u4e0e\u7b14\u8bb0\u672c\u7ea7\u547d\u4ee4\u7ed1\u5b9a\u5728\u4e00\u8d77\uff0c\u5e76\u901a\u8fc7\u4e00\u4e2a\u7070\u6846\u3001\u5de6\u8fb9\u8ddd\u84dd\u8272\u7684\u5355\u5143\u683c\u663e\u793a\u3002"], "Close": ["\u5173\u95ed"], "Keyboard shortcuts": ["\u952e\u76d8\u5feb\u6377\u952e"], "Command": ["\u547d\u4ee4"], "Control": ["\u63a7\u5236"], "Option": ["\u9009\u9879"], "Return": ["\u8fd4\u56de"], "Command Mode (press %s to enable)": ["\u547d\u4ee4\u884c\u6a21\u5f0f\uff08\u6309 %s \u751f\u6548\uff09"], "Edit Shortcuts": ["\u7f16\u8f91\u5feb\u6377\u952e"], "edit command-mode keyboard shortcuts": ["\u7f16\u8f91\u547d\u4ee4\u6a21\u5f0f\u952e\u76d8\u5feb\u6377\u952e"], "Edit Mode (press %s to enable)": ["\u7f16\u8f91\u6a21\u5f0f\uff08\u6309 %s \u751f\u6548\uff09"], "Autosave Failed!": ["\u81ea\u52a8\u4fdd\u5b58\u5931\u8d25\uff01"], "Rename": ["\u91cd\u547d\u540d"], "Enter a new notebook name:": ["\u8bf7\u8f93\u5165\u65b0\u7684\u7b14\u8bb0\u672c\u540d\u79f0:"], "Rename Notebook": ["\u91cd\u547d\u540d\u7b14\u8bb0\u672c"], "Invalid notebook name. Notebook names must have 1 or more characters and can contain any characters except :/\\. Please enter a new notebook name:": ["\u65e0\u6548\u7684\u7b14\u8bb0\u672c\u540d\u79f0\u3002\u7b14\u8bb0\u672c\u540d\u79f0\u4e0d\u80fd\u4e3a\u7a7a\uff0c\u5e76\u4e14\u4e0d\u80fd\u5305\u542b\":/.\"\u3002\u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u7b14\u8bb0\u672c\u540d\u79f0:"], "Renaming...": ["\u6b63\u5728\u91cd\u547d\u540d\u2026"], "Unknown error": ["\u672a\u77e5\u9519\u8bef"], "no checkpoint": ["\u6ca1\u6709\u68c0\u67e5\u70b9"], "Last Checkpoint: %s": ["\u6700\u65b0\u68c0\u67e5\u70b9: %s "], "(unsaved changes)": ["\uff08\u66f4\u6539\u672a\u4fdd\u5b58\uff09"], "(autosaved)": ["\uff08\u5df2\u81ea\u52a8\u4fdd\u5b58\uff09"], "Warning: too many matches (%d). Some changes might not be shown or applied.": ["\u8b66\u544a\uff1a\u592a\u591a\u7684\u5339\u914d(%d)\u3002\u6709\u4e9b\u66f4\u6539\u53ef\u80fd\u4e0d\u4f1a\u88ab\u663e\u793a\u6216\u5e94\u7528."], "%d match": ["%d \u5339\u914d", "%d \u5339\u914d"], "More than 100 matches, aborting": ["\u8d85\u8fc7 100 \u4e2a\u5339\u914d, \u4e2d\u6b62"], "Use regex (JavaScript regex syntax)": ["\u4f7f\u7528\u6b63\u5219\u8868\u8fbe\u5f0f\uff08JavaScript \u6b63\u5219\u8868\u8fbe\u5f0f\u8bed\u6cd5\uff09"], "Replace in selected cells": ["\u5728\u9009\u4e2d\u5355\u5143\u683c\u4e2d\u66ff\u6362"], "Match case": ["\u5339\u914d\u5927\u5c0f\u5199"], "Find": ["\u67e5\u627e"], "Replace": ["\u66ff\u6362"], "No matches, invalid or empty regular expression": ["\u65e0\u5339\u914d\uff0c\u8868\u8fbe\u5f0f\u65e0\u6548\u6216\u8868\u8fbe\u5f0f\u4e3a\u7a7a"], "Replace All": ["\u5168\u90e8\u66ff\u6362"], "Find and Replace": ["\u67e5\u627e\u5e76\u4e14\u66ff\u6362"], "find and replace": ["\u67e5\u627e\u5e76\u4e14\u66ff\u6362"], "Write raw LaTeX or other formats here, for use with nbconvert. It will not be rendered in the notebook. When passing through nbconvert, a Raw Cell's content is added to the output unmodified.": ["\u5728\u8fd9\u91cc\u76f4\u63a5\u5199 LaTeX \u6216\u8005\u5176\u5b83\u683c\u5f0f\u7684\u6587\u672c\u6765\u914d\u5408 nbconvert\u3002\u7b14\u8bb0\u672c\u4e0d\u4f1a\u6e32\u67d3\u5b83\u3002\u4f20\u7ed9 nbconvert \u65f6\uff0c\u539f\u59cb\u5355\u5143\u683c\u7684\u5185\u5bb9\u4f1a\u88ab\u5b8c\u597d\u5730\u52a0\u8fdb\u8f93\u51fa\u3002"], "Grow the tooltip vertically (press shift-tab twice)": ["\u7eb5\u5411\u5c55\u5f00\u5de5\u5177\u63d0\u793a\uff08\u6309\u4e24\u6b21 Shift+Tab\uff09"], "show the current docstring in pager (press shift-tab 4 times)": ["\u5728\u5206\u9875\u5668\u4e2d\u663e\u793a\u5f53\u524d\u7684\u6587\u6863\u5b57\u7b26\u4e32\uff08\u6309\u56db\u6b21 Shift+Tab\uff09"], "Open in Pager": ["\u5728\u5206\u9875\u5668\u4e2d\u6253\u5f00"], "Tooltip will linger for 10 seconds while you type": ["\u5f53\u60a8\u952e\u5165\u65f6\uff0c\u5de5\u5177\u63d0\u793a\u4f1a\u505c\u7559\u5341\u79d2"], "Welcome to the Notebook Tour": ["\u6b22\u8fce\u6765\u5230 Notebook \u5bfc\u89c8"], "You can use the left and right arrow keys to go backwards and forwards.": ["\u4f60\u53ef\u4ee5\u4f7f\u7528\u5de6\u53f3\u7bad\u5934\u952e\u6765\u524d\u540e\u79fb\u52a8"], "Filename": ["\u6587\u4ef6\u540d"], "Click here to change the filename for this notebook.": ["\u70b9\u51fb\u8fd9\u91cc\u4fee\u6539\u7b14\u8bb0\u672c\u7684\u6587\u4ef6\u540d"], "Notebook Menubar": ["\u7b14\u8bb0\u672c\u83dc\u5355\u680f"], "The menubar has menus for actions on the notebook, its cells, and the kernel it communicates with.": ["\u83dc\u5355\u680f\u4e0a\u7684\u83dc\u5355\u53ef\u4ee5\u7528\u6765\u64cd\u4f5c\u7b14\u8bb0\u672c\u3001\u5355\u5143\u683c\u548c\u4e0e\u7b14\u8bb0\u672c\u901a\u4fe1\u7684\u5185\u6838\u3002"], "Notebook Toolbar": ["\u7b14\u8bb0\u672c\u5de5\u5177\u680f"], "The toolbar has buttons for the most common actions. Hover your mouse over each button for more information.": ["\u5de5\u5177\u680f\u6709\u6700\u5e38\u89c1\u64cd\u4f5c\u7684\u6309\u94ae\u3002\u5c06\u9f20\u6807\u60ac\u505c\u5728\u6bcf\u4e2a\u6309\u94ae\u4e0a\u4ee5\u83b7\u5f97\u66f4\u591a\u4fe1\u606f\u3002"], "Mode Indicator": ["\u6a21\u5f0f\u6307\u793a\u5668"], "The Notebook has two modes: Edit Mode and Command Mode. In this area, an indicator can appear to tell you which mode you are in.": ["\u7b14\u8bb0\u672c\u6709\u4e24\u79cd\u6a21\u5f0f\uff1a\u7f16\u8f91\u6a21\u5f0f\u548c\u547d\u4ee4\u6a21\u5f0f\u3002\u5728\u8fd9\u4e2a\u533a\u57df\uff0c\u4e00\u4e2a\u6307\u793a\u5668\u53ef\u4ee5\u663e\u793a\u4f60\u5728\u54ea\u4e2a\u6a21\u5f0f\u3002"], "Right now you are in Command Mode, and many keyboard shortcuts are available. In this mode, no icon is displayed in the indicator area.": ["\u73b0\u5728\u4f60\u5904\u4e8e\u547d\u4ee4\u6a21\u5f0f\uff0c\u8bb8\u591a\u5feb\u6377\u952e\u90fd\u53ef\u4ee5\u4f7f\u7528\u3002\u5728\u8be5\u6a21\u5f0f\u4e0b\uff0c\u6307\u793a\u533a\u57df\u4e2d\u6ca1\u6709\u663e\u793a\u56fe\u6807\u3002"], "Pressing <code>Enter</code> or clicking in the input text area of the cell switches to Edit Mode.": ["\u6309\u4e0b<code>Enter</code>\u6216\u8005\u70b9\u51fb\u8f93\u5165\u6587\u672c\u533a\u57df\u6765\u5207\u6362\u5230\u7f16\u8f91\u6a21\u5f0f. "], "Notice that the border around the currently active cell changed color. Typing will insert text into the currently active cell.": ["\u60a8\u4f1a\u53d1\u73b0\u5f53\u524d\u6d3b\u52a8\u5355\u5143\u683c\u5468\u56f4\u7684\u8fb9\u6846\u6539\u53d8\u4e86\u989c\u8272\u3002\u952e\u5165\u5c06\u5728\u5f53\u524d\u6d3b\u52a8\u5355\u5143\u683c\u4e2d\u63d2\u5165\u6587\u672c."], "Back to Command Mode": ["\u56de\u5230\u547d\u4ee4\u6a21\u5f0f"], "Pressing <code>Esc</code> or clicking outside of the input text area takes you back to Command Mode.": ["\u6309\u4e0b<code>Esc</code>\u6216\u8005\u70b9\u51fb\u8f93\u5165\u6846\u5916\u9762\u6765\u8fd4\u56de\u5230\u547d\u4ee4\u6a21\u5f0f\u3002"], "Keyboard Shortcuts": ["\u952e\u76d8\u5feb\u6377\u952e"], "You can click here to get a list of all of the keyboard shortcuts.": ["\u70b9\u51fb\u8fd9\u91cc\u83b7\u5f97\u6240\u6709\u952e\u76d8\u5feb\u6377\u952e"], "Kernel Indicator": ["\u5185\u6838\u6307\u793a\u5668"], "This is the Kernel indicator. It looks like this when the Kernel is idle.": ["\u8fd9\u662f\u5185\u6838\u6307\u793a\u5668\u3002\u5f53\u5185\u6838\u7a7a\u95f2\u65f6\uff0c\u5b83\u770b\u8d77\u6765\u5c31\u50cf\u8fd9\u6837\u3002"], "The Kernel indicator looks like this when the Kernel is busy.": ["\u5185\u6838\u6307\u793a\u5668\u5728\u5185\u6838\u7e41\u5fd9\u65f6\u770b\u8d77\u6765\u662f\u8fd9\u6837\u7684\u3002"], "Interrupting the Kernel": ["\u5185\u6838\u4e2d\u65ad"], "To cancel a computation in progress, you can click here.": ["\u8981\u53d6\u6d88\u6b63\u5728\u8fdb\u884c\u7684\u8ba1\u7b97\u4efb\u52a1\uff0c\u60a8\u53ef\u4ee5\u70b9\u51fb\u8fd9\u91cc\u3002"], "Notification Area": ["\u4efb\u52a1\u680f\u901a\u77e5\u533a"], "Messages in response to user actions (Save, Interrupt, etc.) appear here.": ["\u54cd\u5e94\u7528\u6237\u64cd\u4f5c\uff08\u4fdd\u5b58\uff0c\u4e2d\u65ad\u7b49\uff09\u7684\u6d88\u606f\u51fa\u73b0\u5728\u8fd9\u91cc\u3002"], "End of Tour": ["\u7ed3\u675f\u5bfc\u89c8"], "This concludes the Jupyter Notebook User Interface Tour.": ["Jupyter \u7b14\u8bb0\u672c\u7528\u6237\u754c\u9762\u4e4b\u65c5\u5230\u6b64\u4e3a\u6b62\u3002"], "Edit Attachments": ["\u7f16\u8f91\u9644\u4ef6"], "Cell": ["\u5355\u5143\u683c"], "Edit Metadata": ["\u7f16\u8f91\u5143\u6570\u636e"], "Custom": ["\u81ea\u5b9a\u4e49"], "Set the MIME type of the raw cell:": ["\u8bbe\u7f6e\u539f\u59cb\u5355\u5143\u683c\u7684 MIME \u7c7b\u578b\uff1a"], "Raw Cell MIME Type": ["\u539f\u59cb\u5355\u5143\u683c\u7684 MIME \u7c7b\u578b"], "Raw NBConvert Format": ["\u539f\u59cb NBConvert \u7c7b\u578b"], "Raw Cell Format": ["\u539f\u59cb\u5355\u5143\u683c\u683c\u5f0f"], "Slide": ["\u5e7b\u706f\u7247"], "Sub-Slide": ["\u5b50\u5e7b\u706f\u7247"], "Fragment": ["\u788e\u7247"], "Skip": ["\u8df3\u8fc7"], "Notes": ["\u4ee3\u7801"], "Slide Type": ["\u5e7b\u706f\u7247\u7c7b\u578b"], "Slideshow": ["\u5e7b\u706f\u7247"], "Add tag": ["\u6dfb\u52a0\u6807\u7b7e"], "Edit the list of tags below. All whitespace is treated as tag separators.": ["\u7f16\u8f91\u4e0b\u9762\u7684\u6807\u7b7e\u5217\u8868\u3002\u6240\u6709\u7a7a\u683c\u90fd\u88ab\u5f53\u4f5c\u6807\u8bb0\u5206\u9694\u7b26\u3002"], "Edit the tags": ["\u7f16\u8f91\u6807\u7b7e"], "Edit Tags": ["\u7f16\u8f91\u6807\u7b7e"], "Shutdown": ["\u5173\u95ed"], "Create a new notebook with %s": ["\u521b\u5efa\u65b0\u7684\u7b14\u8bb0\u672c %s"], "An error occurred while creating a new notebook.": ["\u521b\u5efa\u65b0\u7b14\u8bb0\u672c\u65f6\u51fa\u9519\u3002"], "Creating File Failed": ["\u521b\u5efa\u6587\u4ef6\u5931\u8d25"], "An error occurred while creating a new file.": ["\u521b\u5efa\u65b0\u6587\u4ef6\u65f6\u51fa\u9519\u3002"], "Creating Folder Failed": ["\u521b\u5efa\u6587\u4ef6\u5939\u5931\u8d25"], "An error occurred while creating a new folder.": ["\u521b\u5efa\u65b0\u6587\u4ef6\u5939\u65f6\u51fa\u9519\u3002"], "Failed to read file": ["\u8bfb\u53d6\u6587\u4ef6\u5931\u8d25"], "Failed to read file %s": ["\u8bfb\u53d6\u6587\u4ef6 %s \u5931\u8d25\u4e86"], "The file size is %d MB. Do you still want to upload it?": ["\u6587\u4ef6\u5927\u5c0f\u4e3a %d MB\uff0c\u4f9d\u7136\u4e0a\u4f20?"], "Large file size warning": ["\u8bf7\u6ce8\u610f\u6587\u4ef6\u5927\u5c0f"], "Server error: ": ["\u670d\u52a1\u51fa\u73b0\u9519\u8bef\uff1a"], "The notebook list is empty.": ["\u7b14\u8bb0\u672c\u5217\u8868\u4e3a\u7a7a\u3002"], "Click here to rename, delete, etc.": ["\u70b9\u51fb\u8fd9\u91cc\u8fdb\u884c\u91cd\u547d\u540d\u6216\u5220\u9664\u7b49\u64cd\u4f5c"], "Running": ["\u8fd0\u884c"], "Enter a new file name:": ["\u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u6587\u4ef6\u540d\uff1a"], "Enter a new directory name:": ["\u8bf7\u8f93\u5165\u4e00\u4e2a\u65b0\u7684\u8def\u5f84\uff1a"], "Enter a new name:": ["\u8bf7\u8f93\u5165\u65b0\u540d\u5b57\uff1a"], "Rename file": ["\u6587\u4ef6\u91cd\u547d\u540d"], "Rename directory": ["\u91cd\u547d\u540d\u8def\u5f84"], "Rename notebook": ["\u91cd\u547d\u540d\u7b14\u8bb0\u672c"], "Move": ["\u79fb\u52a8"], "An error occurred while renaming \"%1$s\" to \"%2$s\".": ["\u5f53\u628a \"%1$s\" \u91cd\u547d\u540d\u4e3a \"%2$s\" \u65f6\u51fa\u73b0\u9519\u8bef."], "Rename Failed": ["\u91cd\u547d\u540d\u5931\u8d25"], "Enter a new destination directory path for this item:": ["\u4e3a\u7b14\u8bb0\u672c\u9009\u62e9\u4e00\u4e2a\u65b0\u7684\u8def\u5f84\uff1a", "\u4e3a\u9009\u4e2d\u7684 %d \u7b14\u8bb0\u672c\u9009\u62e9\u4e00\u4e2a\u65b0\u7684\u8def\u5f84\uff1a"], "Move an Item": ["\u79fb\u52a8\u4e00\u4e2a\u6587\u4ef6", "\u79fb\u52a8 %d \u4e2a\u6587\u4ef6"], "An error occurred while moving \"%1$s\" from \"%2$s\" to \"%3$s\".": ["\u5f53\u628a \"%1$s\" \u4ece \"%2$s\" \u79fb\u52a8\u5230 \"%3$s\" \u65f6\u51fa\u73b0\u9519\u8bef."], "Move Failed": ["\u79fb\u52a8\u5931\u8d25"], "Are you sure you want to permanently delete: \"%s\"?": ["\u786e\u5b9a\u6c38\u4e45\u5220\u9664 \"%s\"?", "\u786e\u5b9a\u6c38\u4e45\u5220\u9664\u9009\u4e2d\u7684 %d \u4e2a\u6587\u4ef6\u6216\u6587\u4ef6\u5939?"], "An error occurred while deleting \"%s\".": ["\u5f53\u5220\u9664 \"%s\" \u65f6, \u51fa\u73b0\u9519\u8bef\u3002"], "Delete Failed": ["\u5220\u9664\u5931\u8d25"], "Are you sure you want to duplicate: \"%s\"?": ["\u786e\u5b9a\u5236\u4f5c \"%s\" \u7684\u526f\u672c\uff1f", "\u786e\u5b9a\u5236\u4f5c\u9009\u4e2d\u7684 %d \u4e2a\u6587\u4ef6\u7684\u526f\u672c?"], "Duplicate": ["\u5236\u4f5c\u526f\u672c"], "An error occurred while duplicating \"%s\".": ["\u5236\u4f5c \"%s\" \u7684\u526f\u672c\u65f6\u51fa\u73b0\u9519\u8bef\u3002"], "Duplicate Failed": ["\u5236\u4f5c\u526f\u672c\u5931\u8d25"], "Upload": ["\u4e0a\u4f20"], "Invalid file name": ["\u65e0\u6548\u7684\u6587\u4ef6\u540d"], "File names must be at least one character and not start with a period": ["\u6587\u4ef6\u540d\u4e0d\u80fd\u4e3a\u7a7a\uff0c\u5e76\u4e14\u4e0d\u80fd\u4ee5\u53e5\u53f7\u5f00\u59cb\uff0c\u9664\u4e0b\u5212\u7ebf\u4ee5\u5916\u7684\u7b26\u53f7\u90fd\u4e0d\u80fd\u5f00\u5934"], "Cannot upload invalid Notebook": ["\u65e0\u6cd5\u4e0a\u4f20\u65e0\u6548\u7684\u7b14\u8bb0\u672c"], "There is already a file named \"%s\". Do you want to replace it?": ["\u5df2\u7ecf\u5b58\u5728\u4e00\u4e2a\u540d\u4e3a \"%s\" \u7684\u6587\u4ef6\uff0c\u66ff\u6362\u73b0\u6709\u6587\u4ef6\uff1f"], "Replace file": ["\u66ff\u6362\u6587\u4ef6"]}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./21大数据张兆鹤-二元函数梯度下降_files/contents.js.下载"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888; display: contents}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./21大数据张兆鹤-二元函数梯度下降_files/custom.js.下载"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="nbextensions/jupyter-js-widgets/extension" src="./21大数据张兆鹤-二元函数梯度下降_files/extension.js.下载"></script><style type="text/css">div.MathJax_MathML {text-align: center; margin: .75em 0px; display: block!important}
.MathJax_MathML {font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
span.MathJax_MathML {display: inline!important}
.MathJax_mmlExBox {display: block!important; overflow: hidden; height: 1px; width: 60ex; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0}
[class="MJX-tex-oldstyle"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-oldstyle-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
[class="MJX-tex-caligraphic"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB}
[class="MJX-tex-caligraphic-bold"] {font-family: MathJax_Caligraphic, MathJax_Caligraphic-WEB; font-weight: bold}
@font-face /*1*/ {font-family: MathJax_Caligraphic-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf')}
@font-face /*2*/ {font-family: MathJax_Caligraphic-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Bold.otf')}
[mathvariant="double-struck"] {font-family: MathJax_AMS, MathJax_AMS-WEB}
[mathvariant="script"] {font-family: MathJax_Script, MathJax_Script-WEB}
[mathvariant="fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB}
[mathvariant="bold-script"] {font-family: MathJax_Script, MathJax_Caligraphic-WEB; font-weight: bold}
[mathvariant="bold-fraktur"] {font-family: MathJax_Fraktur, MathJax_Fraktur-WEB; font-weight: bold}
[mathvariant="monospace"] {font-family: monospace}
[mathvariant="sans-serif"] {font-family: sans-serif}
[mathvariant="bold-sans-serif"] {font-family: sans-serif; font-weight: bold}
[mathvariant="sans-serif-italic"] {font-family: sans-serif; font-style: italic}
[mathvariant="sans-serif-bold-italic"] {font-family: sans-serif; font-style: italic; font-weight: bold}
@font-face /*3*/ {font-family: MathJax_AMS-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_AMS-Regular.otf')}
@font-face /*4*/ {font-family: MathJax_Script-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Script-Regular.otf')}
@font-face /*5*/ {font-family: MathJax_Fraktur-WEB; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Regular.otf')}
@font-face /*6*/ {font-family: MathJax_Fraktur-WEB; font-weight: bold; src: url('http://localhost:8888/static/components/MathJax/fonts/HTML-CSS/TeX/otf/MathJax_Fraktur-Bold.otf')}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Blank; src: url('about:blank')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/* Override the correction for the prompt area in https://github.com/jupyter/notebook/blob/dd41d9fd5c4f698bd7468612d877828a7eeb0e7a/IPython/html/static/notebook/less/outputarea.less#L110 */
.jupyter-widgets-output-area div.output_subarea {
    max-width: 100%;
}

/* Work-around for the bug fixed in https://github.com/jupyter/notebook/pull/2961 */
.jupyter-widgets-output-area > .out_prompt_overlay {
    display: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


.p-Widget.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-CommandPalette-search {
  flex: 0 0 auto;
}


.p-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


.p-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


.p-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


.p-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


.p-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


.p-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


.p-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-DockPanel {
  z-index: 0;
}


.p-DockPanel-widget {
  z-index: 0;
}


.p-DockPanel-tabBar {
  z-index: 1;
}


.p-DockPanel-handle {
  z-index: 2;
}


.p-DockPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


.p-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


.p-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


.p-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


.p-DockPanel-overlay.p-mod-hidden {
  display: none !important;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


.p-Menu-item {
  display: table-row;
}


.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed {
  display: none !important;
}


.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


.p-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


.p-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


.p-MenuBar-item {
  box-sizing: border-box;
}


.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel {
  display: inline-block;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


.p-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


.p-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-SplitPanel-child {
  z-index: 0;
}


.p-SplitPanel-handle {
  z-index: 1;
}


.p-SplitPanel-handle.p-mod-hidden {
  display: none !important;
}


.p-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle {
  cursor: ew-resize;
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle {
  cursor: ns-resize;
}


.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


.p-TabPanel-tabBar {
  z-index: 1;
}


.p-TabPanel-stackedPanel {
  z-index: 0;
}
</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

 .jupyter-widgets-disconnected::before {
    content: "\f127"; /* chain-broken */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #d9534f;
    padding: 3px;
    align-self: flex-start;
}
</style><style type="text/css">/**
 * The material design colors are adapted from google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/dist/palette.var.css
 *
 * The license for the material design color CSS variables is as follows (see
 * https://github.com/danlevan/google-material-color/blob/f67ca5f4028b2f1b34862f64b0ca67323f91b088/LICENSE)
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 Dan Le Van
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
:root {
  --md-red-50: #FFEBEE;
  --md-red-100: #FFCDD2;
  --md-red-200: #EF9A9A;
  --md-red-300: #E57373;
  --md-red-400: #EF5350;
  --md-red-500: #F44336;
  --md-red-600: #E53935;
  --md-red-700: #D32F2F;
  --md-red-800: #C62828;
  --md-red-900: #B71C1C;
  --md-red-A100: #FF8A80;
  --md-red-A200: #FF5252;
  --md-red-A400: #FF1744;
  --md-red-A700: #D50000;

  --md-pink-50: #FCE4EC;
  --md-pink-100: #F8BBD0;
  --md-pink-200: #F48FB1;
  --md-pink-300: #F06292;
  --md-pink-400: #EC407A;
  --md-pink-500: #E91E63;
  --md-pink-600: #D81B60;
  --md-pink-700: #C2185B;
  --md-pink-800: #AD1457;
  --md-pink-900: #880E4F;
  --md-pink-A100: #FF80AB;
  --md-pink-A200: #FF4081;
  --md-pink-A400: #F50057;
  --md-pink-A700: #C51162;

  --md-purple-50: #F3E5F5;
  --md-purple-100: #E1BEE7;
  --md-purple-200: #CE93D8;
  --md-purple-300: #BA68C8;
  --md-purple-400: #AB47BC;
  --md-purple-500: #9C27B0;
  --md-purple-600: #8E24AA;
  --md-purple-700: #7B1FA2;
  --md-purple-800: #6A1B9A;
  --md-purple-900: #4A148C;
  --md-purple-A100: #EA80FC;
  --md-purple-A200: #E040FB;
  --md-purple-A400: #D500F9;
  --md-purple-A700: #AA00FF;

  --md-deep-purple-50: #EDE7F6;
  --md-deep-purple-100: #D1C4E9;
  --md-deep-purple-200: #B39DDB;
  --md-deep-purple-300: #9575CD;
  --md-deep-purple-400: #7E57C2;
  --md-deep-purple-500: #673AB7;
  --md-deep-purple-600: #5E35B1;
  --md-deep-purple-700: #512DA8;
  --md-deep-purple-800: #4527A0;
  --md-deep-purple-900: #311B92;
  --md-deep-purple-A100: #B388FF;
  --md-deep-purple-A200: #7C4DFF;
  --md-deep-purple-A400: #651FFF;
  --md-deep-purple-A700: #6200EA;

  --md-indigo-50: #E8EAF6;
  --md-indigo-100: #C5CAE9;
  --md-indigo-200: #9FA8DA;
  --md-indigo-300: #7986CB;
  --md-indigo-400: #5C6BC0;
  --md-indigo-500: #3F51B5;
  --md-indigo-600: #3949AB;
  --md-indigo-700: #303F9F;
  --md-indigo-800: #283593;
  --md-indigo-900: #1A237E;
  --md-indigo-A100: #8C9EFF;
  --md-indigo-A200: #536DFE;
  --md-indigo-A400: #3D5AFE;
  --md-indigo-A700: #304FFE;

  --md-blue-50: #E3F2FD;
  --md-blue-100: #BBDEFB;
  --md-blue-200: #90CAF9;
  --md-blue-300: #64B5F6;
  --md-blue-400: #42A5F5;
  --md-blue-500: #2196F3;
  --md-blue-600: #1E88E5;
  --md-blue-700: #1976D2;
  --md-blue-800: #1565C0;
  --md-blue-900: #0D47A1;
  --md-blue-A100: #82B1FF;
  --md-blue-A200: #448AFF;
  --md-blue-A400: #2979FF;
  --md-blue-A700: #2962FF;

  --md-light-blue-50: #E1F5FE;
  --md-light-blue-100: #B3E5FC;
  --md-light-blue-200: #81D4FA;
  --md-light-blue-300: #4FC3F7;
  --md-light-blue-400: #29B6F6;
  --md-light-blue-500: #03A9F4;
  --md-light-blue-600: #039BE5;
  --md-light-blue-700: #0288D1;
  --md-light-blue-800: #0277BD;
  --md-light-blue-900: #01579B;
  --md-light-blue-A100: #80D8FF;
  --md-light-blue-A200: #40C4FF;
  --md-light-blue-A400: #00B0FF;
  --md-light-blue-A700: #0091EA;

  --md-cyan-50: #E0F7FA;
  --md-cyan-100: #B2EBF2;
  --md-cyan-200: #80DEEA;
  --md-cyan-300: #4DD0E1;
  --md-cyan-400: #26C6DA;
  --md-cyan-500: #00BCD4;
  --md-cyan-600: #00ACC1;
  --md-cyan-700: #0097A7;
  --md-cyan-800: #00838F;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84FFFF;
  --md-cyan-A200: #18FFFF;
  --md-cyan-A400: #00E5FF;
  --md-cyan-A700: #00B8D4;

  --md-teal-50: #E0F2F1;
  --md-teal-100: #B2DFDB;
  --md-teal-200: #80CBC4;
  --md-teal-300: #4DB6AC;
  --md-teal-400: #26A69A;
  --md-teal-500: #009688;
  --md-teal-600: #00897B;
  --md-teal-700: #00796B;
  --md-teal-800: #00695C;
  --md-teal-900: #004D40;
  --md-teal-A100: #A7FFEB;
  --md-teal-A200: #64FFDA;
  --md-teal-A400: #1DE9B6;
  --md-teal-A700: #00BFA5;

  --md-green-50: #E8F5E9;
  --md-green-100: #C8E6C9;
  --md-green-200: #A5D6A7;
  --md-green-300: #81C784;
  --md-green-400: #66BB6A;
  --md-green-500: #4CAF50;
  --md-green-600: #43A047;
  --md-green-700: #388E3C;
  --md-green-800: #2E7D32;
  --md-green-900: #1B5E20;
  --md-green-A100: #B9F6CA;
  --md-green-A200: #69F0AE;
  --md-green-A400: #00E676;
  --md-green-A700: #00C853;

  --md-light-green-50: #F1F8E9;
  --md-light-green-100: #DCEDC8;
  --md-light-green-200: #C5E1A5;
  --md-light-green-300: #AED581;
  --md-light-green-400: #9CCC65;
  --md-light-green-500: #8BC34A;
  --md-light-green-600: #7CB342;
  --md-light-green-700: #689F38;
  --md-light-green-800: #558B2F;
  --md-light-green-900: #33691E;
  --md-light-green-A100: #CCFF90;
  --md-light-green-A200: #B2FF59;
  --md-light-green-A400: #76FF03;
  --md-light-green-A700: #64DD17;

  --md-lime-50: #F9FBE7;
  --md-lime-100: #F0F4C3;
  --md-lime-200: #E6EE9C;
  --md-lime-300: #DCE775;
  --md-lime-400: #D4E157;
  --md-lime-500: #CDDC39;
  --md-lime-600: #C0CA33;
  --md-lime-700: #AFB42B;
  --md-lime-800: #9E9D24;
  --md-lime-900: #827717;
  --md-lime-A100: #F4FF81;
  --md-lime-A200: #EEFF41;
  --md-lime-A400: #C6FF00;
  --md-lime-A700: #AEEA00;

  --md-yellow-50: #FFFDE7;
  --md-yellow-100: #FFF9C4;
  --md-yellow-200: #FFF59D;
  --md-yellow-300: #FFF176;
  --md-yellow-400: #FFEE58;
  --md-yellow-500: #FFEB3B;
  --md-yellow-600: #FDD835;
  --md-yellow-700: #FBC02D;
  --md-yellow-800: #F9A825;
  --md-yellow-900: #F57F17;
  --md-yellow-A100: #FFFF8D;
  --md-yellow-A200: #FFFF00;
  --md-yellow-A400: #FFEA00;
  --md-yellow-A700: #FFD600;

  --md-amber-50: #FFF8E1;
  --md-amber-100: #FFECB3;
  --md-amber-200: #FFE082;
  --md-amber-300: #FFD54F;
  --md-amber-400: #FFCA28;
  --md-amber-500: #FFC107;
  --md-amber-600: #FFB300;
  --md-amber-700: #FFA000;
  --md-amber-800: #FF8F00;
  --md-amber-900: #FF6F00;
  --md-amber-A100: #FFE57F;
  --md-amber-A200: #FFD740;
  --md-amber-A400: #FFC400;
  --md-amber-A700: #FFAB00;

  --md-orange-50: #FFF3E0;
  --md-orange-100: #FFE0B2;
  --md-orange-200: #FFCC80;
  --md-orange-300: #FFB74D;
  --md-orange-400: #FFA726;
  --md-orange-500: #FF9800;
  --md-orange-600: #FB8C00;
  --md-orange-700: #F57C00;
  --md-orange-800: #EF6C00;
  --md-orange-900: #E65100;
  --md-orange-A100: #FFD180;
  --md-orange-A200: #FFAB40;
  --md-orange-A400: #FF9100;
  --md-orange-A700: #FF6D00;

  --md-deep-orange-50: #FBE9E7;
  --md-deep-orange-100: #FFCCBC;
  --md-deep-orange-200: #FFAB91;
  --md-deep-orange-300: #FF8A65;
  --md-deep-orange-400: #FF7043;
  --md-deep-orange-500: #FF5722;
  --md-deep-orange-600: #F4511E;
  --md-deep-orange-700: #E64A19;
  --md-deep-orange-800: #D84315;
  --md-deep-orange-900: #BF360C;
  --md-deep-orange-A100: #FF9E80;
  --md-deep-orange-A200: #FF6E40;
  --md-deep-orange-A400: #FF3D00;
  --md-deep-orange-A700: #DD2C00;

  --md-brown-50: #EFEBE9;
  --md-brown-100: #D7CCC8;
  --md-brown-200: #BCAAA4;
  --md-brown-300: #A1887F;
  --md-brown-400: #8D6E63;
  --md-brown-500: #795548;
  --md-brown-600: #6D4C41;
  --md-brown-700: #5D4037;
  --md-brown-800: #4E342E;
  --md-brown-900: #3E2723;

  --md-grey-50: #FAFAFA;
  --md-grey-100: #F5F5F5;
  --md-grey-200: #EEEEEE;
  --md-grey-300: #E0E0E0;
  --md-grey-400: #BDBDBD;
  --md-grey-500: #9E9E9E;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #ECEFF1;
  --md-blue-grey-100: #CFD8DC;
  --md-blue-grey-200: #B0BEC5;
  --md-blue-grey-300: #90A4AE;
  --md-blue-grey-400: #78909C;
  --md-blue-grey-500: #607D8B;
  --md-blue-grey-600: #546E7A;
  --md-blue-grey-700: #455A64;
  --md-blue-grey-800: #37474F;
  --md-blue-grey-900: #263238;
}</style><style type="text/css">/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
This file is copied from the JupyterLab project to define default styling for
when the widget styling is compiled down to eliminate CSS variables. We make one
change - we comment out the font import below.
*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/


/*
 * Optional monospace font for input/output prompt.
 */
 /* Commented out in ipywidgets since we don't need it. */
/* @import url('https://fonts.googleapis.com/css?family=Roboto+Mono'); */

/*
 * Added for compabitility with output area
 */
:root {
  --jp-icon-search: none;
  --jp-ui-select-caret: none;
}


:root {

  /* Borders

  The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-700);
  --jp-border-color1: var(--md-grey-500);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-100);

  /* UI Fonts

  The UI font CSS variables are used for the typography all of the JupyterLab
  user interface elements that are not directly user generated content.
  */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));
  --jp-ui-icon-font-size: 14px; /* Ensures px perfect FontAwesome icons */
  --jp-ui-font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;

  /* Use these font colors against the corresponding main layout colors.
     In a light theme, these go from dark to light.
  */

  --jp-ui-font-color0: rgba(0,0,0,1.0);
  --jp-ui-font-color1: rgba(0,0,0,0.8);
  --jp-ui-font-color2: rgba(0,0,0,0.5);
  --jp-ui-font-color3: rgba(0,0,0,0.3);

  /* Use these against the brand/accent/warn/error colors.
     These will typically go from light to darker, in both a dark and light theme
   */

  --jp-inverse-ui-font-color0: rgba(255,255,255,1);
  --jp-inverse-ui-font-color1: rgba(255,255,255,1.0);
  --jp-inverse-ui-font-color2: rgba(255,255,255,0.7);
  --jp-inverse-ui-font-color3: rgba(255,255,255,0.5);

  /* Content Fonts

  Content font variables are used for typography of user generated content.
  */

  --jp-content-font-size: 13px;
  --jp-content-line-height: 1.5;
  --jp-content-font-color0: black;
  --jp-content-font-color1: black;
  --jp-content-font-color2: var(--md-grey-700);
  --jp-content-font-color3: var(--md-grey-500);

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: calc(var(--jp-ui-font-size1)/var(--jp-ui-font-scale-factor));
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: calc(var(--jp-ui-font-size1)*var(--jp-ui-font-scale-factor));
  --jp-ui-font-size3: calc(var(--jp-ui-font-size2)*var(--jp-ui-font-scale-factor));

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.307;
  --jp-code-padding: 5px;
  --jp-code-font-family: monospace;


  /* Layout

  The following are the main layout colors use in JupyterLab. In a light
  theme these would go from light to dark.
  */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-700);
  --jp-brand-color1: var(--md-blue-500);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);

  --jp-accent-color0: var(--md-green-700);
  --jp-accent-color1: var(--md-green-500);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-700);
  --jp-warn-color1: var(--md-orange-500);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-700);
  --jp-error-color1: var(--md-red-500);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-700);
  --jp-success-color1: var(--md-green-500);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-700);
  --jp-info-color1: var(--md-cyan-500);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-editor-background: #f7f7f7;
  --jp-cell-editor-border-color: #cfcfcf;
  --jp-cell-editor-background-edit: var(--jp-ui-layout-color1);
  --jp-cell-editor-border-color-edit: var(--jp-brand-color1);
  --jp-cell-prompt-width: 100px;
  --jp-cell-prompt-font-family: 'Roboto Mono', monospace;
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1.0;
  --jp-cell-prompt-opacity-not-active: 0.4;
  --jp-cell-prompt-font-color-not-active: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307FC1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #BF5B3D;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-scroll-padding: 100px;

  /* Console specific styles */

  --jp-console-background: var(--md-grey-100);

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--md-grey-400);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color0);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0,0,0,0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);
}
</style><style type="text/css">/* This file has code derived from PhosphorJS CSS files, as noted below. The license for this PhosphorJS code is:

Copyright (c) 2014-2017, PhosphorJS Contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

*/

/*
 * The following section is derived from https://github.com/phosphorjs/phosphor/blob/23b9d075ebc5b73ab148b6ebfc20af97f85714c4/packages/widgets/style/tabbar.css 
 * We've scoped the rules so that they are consistent with exactly our code.
 */

.jupyter-widgets.widget-tab > .p-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='horizontal'] > .p-TabBar-content {
  flex-direction: row;
}


.jupyter-widgets.widget-tab > .p-TabBar[data-orientation='vertical'] > .p-TabBar-content {
  flex-direction: column;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-hidden {
  display: none !important;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab {
  position: relative;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


.jupyter-widgets.widget-tab > .p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging {
  transition: none;
}

/* End tabbar.css */
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * We assume that the CSS variables in
 * https://github.com/jupyterlab/jupyterlab/blob/master/src/default-theme/variables.css
 * have been defined.
 */

:root {
    --jp-widgets-color: var(--jp-content-font-color1);
    --jp-widgets-label-color: var(--jp-widgets-color);
    --jp-widgets-readout-color: var(--jp-widgets-color);
    --jp-widgets-font-size: var(--jp-ui-font-size1);
    --jp-widgets-margin: 2px;
    --jp-widgets-inline-height: 28px;
    --jp-widgets-inline-width: 300px;
    --jp-widgets-inline-width-short: calc(var(--jp-widgets-inline-width) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-width-tiny: calc(var(--jp-widgets-inline-width-short) / 2 - var(--jp-widgets-margin));
    --jp-widgets-inline-margin: 4px; /* margin between inline elements */
    --jp-widgets-inline-label-width: 80px;
    --jp-widgets-border-width: var(--jp-border-width);
    --jp-widgets-vertical-height: 200px;
    --jp-widgets-horizontal-tab-height: 24px;
    --jp-widgets-horizontal-tab-width: 144px;
    --jp-widgets-horizontal-tab-top-border: 2px;
    --jp-widgets-progress-thickness: 20px;
    --jp-widgets-container-padding: 15px;
    --jp-widgets-input-padding: 4px;
    --jp-widgets-radio-item-height-adjustment: 8px;
    --jp-widgets-radio-item-height: calc(var(--jp-widgets-inline-height) - var(--jp-widgets-radio-item-height-adjustment));
    --jp-widgets-slider-track-thickness: 4px;
    --jp-widgets-slider-border-width: var(--jp-widgets-border-width);
    --jp-widgets-slider-handle-size: 16px;
    --jp-widgets-slider-handle-border-color: var(--jp-border-color1);
    --jp-widgets-slider-handle-background-color: var(--jp-layout-color1);
    --jp-widgets-slider-active-handle-color: var(--jp-brand-color1);
    --jp-widgets-menu-item-height: 24px;
    --jp-widgets-dropdown-arrow: url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE5LjIuMSwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPgo8c3ZnIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4IgoJIHZpZXdCb3g9IjAgMCAxOCAxOCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgMTggMTg7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KPC9zdHlsZT4KPHBhdGggZD0iTTUuMiw1LjlMOSw5LjdsMy44LTMuOGwxLjIsMS4ybC00LjksNWwtNC45LTVMNS4yLDUuOXoiLz4KPHBhdGggY2xhc3M9InN0MCIgZD0iTTAtMC42aDE4djE4SDBWLTAuNnoiLz4KPC9zdmc+Cg");
    --jp-widgets-input-color: var(--jp-ui-font-color1);
    --jp-widgets-input-background-color: var(--jp-layout-color1);
    --jp-widgets-input-border-color: var(--jp-border-color1);
    --jp-widgets-input-focus-border-color: var(--jp-brand-color2);
    --jp-widgets-input-border-width: var(--jp-widgets-border-width);
    --jp-widgets-disabled-opacity: 0.6;

    /* From Material Design Lite */
    --md-shadow-key-umbra-opacity: 0.2;
    --md-shadow-key-penumbra-opacity: 0.14;
    --md-shadow-ambient-shadow-opacity: 0.12;
}

.jupyter-widgets {
    margin: var(--jp-widgets-margin);
    box-sizing: border-box;
    color: var(--jp-widgets-color);
    overflow: visible;
}

.jupyter-widgets.jupyter-widgets-disconnected::before {
    line-height: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
}

.jp-Output-result > .jupyter-widgets {
    margin-left: 0;
    margin-right: 0;
}

/* vbox and hbox */

.widget-inline-hbox {
    /* Horizontal widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    align-items: baseline;
}

.widget-inline-vbox {
    /* Vertical Widgets */
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.widget-box {
    box-sizing: border-box;
    display: flex;
    margin: 0;
    overflow: auto;
}

.widget-gridbox {
    box-sizing: border-box;
    display: grid;
    margin: 0;
    overflow: auto;
}

.widget-hbox {
    flex-direction: row;
}

.widget-vbox {
    flex-direction: column;
}

/* General Button Styling */

.jupyter-button {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
    display: inline-block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    font-size: var(--jp-widgets-font-size);
    cursor: pointer;

    height: var(--jp-widgets-inline-height);
    border: 0px solid;
    line-height: var(--jp-widgets-inline-height);
    box-shadow: none;

    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color2);
    border-color: var(--jp-border-color2);
    border: none;
    user-select: none;
}

.jupyter-button i.fa {
    margin-right: var(--jp-widgets-inline-margin);
    pointer-events: none;
}

.jupyter-button:empty:before {
    content: "\200b"; /* zero-width space */
}

.jupyter-widgets.jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.jupyter-button i.fa.center {
    margin-right: 0;
}

.jupyter-button:hover:enabled, .jupyter-button:focus:enabled {
    /* MD Lite 2dp shadow */
    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 3px 1px -2px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity)),
                0 1px 5px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity));
}

.jupyter-button:active, .jupyter-button.mod-active {
    /* MD Lite 4dp shadow */
    box-shadow: 0 4px 5px 0 rgba(0, 0, 0, var(--md-shadow-key-penumbra-opacity)),
                0 1px 10px 0 rgba(0, 0, 0, var(--md-shadow-ambient-shadow-opacity)),
                0 2px 4px -1px rgba(0, 0, 0, var(--md-shadow-key-umbra-opacity));
    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color3);
}

.jupyter-button:focus:enabled {
    outline: 1px solid var(--jp-widgets-input-focus-border-color);
}

/* Button "Primary" Styling */

.jupyter-button.mod-primary {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-brand-color1);
}

.jupyter-button.mod-primary.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

.jupyter-button.mod-primary:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-brand-color0);
}

/* Button "Success" Styling */

.jupyter-button.mod-success {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-success-color1);
}

.jupyter-button.mod-success.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

.jupyter-button.mod-success:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-success-color0);
 }

 /* Button "Info" Styling */

.jupyter-button.mod-info {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-info-color1);
}

.jupyter-button.mod-info.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

.jupyter-button.mod-info:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-info-color0);
}

/* Button "Warning" Styling */

.jupyter-button.mod-warning {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-warn-color1);
}

.jupyter-button.mod-warning.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

.jupyter-button.mod-warning:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-warn-color0);
}

/* Button "Danger" Styling */

.jupyter-button.mod-danger {
    color: var(--jp-inverse-ui-font-color1);
    background-color: var(--jp-error-color1);
}

.jupyter-button.mod-danger.mod-active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

.jupyter-button.mod-danger:active {
    color: var(--jp-inverse-ui-font-color0);
    background-color: var(--jp-error-color0);
}

/* Widget Button, Widget Toggle Button, Widget Upload */

.widget-button, .widget-toggle-button, .widget-upload {
    width: var(--jp-widgets-inline-width-short);
}

/* Widget Label Styling */

/* Override Bootstrap label css */
.jupyter-widgets label {
    margin-bottom: initial;
}

.widget-label-basic {
    /* Basic Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-label {
    /* Label */
    color: var(--jp-widgets-label-color);
    font-size: var(--jp-widgets-font-size);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    line-height: var(--jp-widgets-inline-height);
}

.widget-inline-hbox .widget-label {
    /* Horizontal Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: right;
    margin-right: calc( var(--jp-widgets-inline-margin) * 2 );
    width: var(--jp-widgets-inline-label-width);
    flex-shrink: 0;
}

.widget-inline-vbox .widget-label {
    /* Vertical Widget Label */
    color: var(--jp-widgets-label-color);
    text-align: center;
    line-height: var(--jp-widgets-inline-height);
}

/* Widget Readout Styling */

.widget-readout {
    color: var(--jp-widgets-readout-color);
    font-size: var(--jp-widgets-font-size);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
}

.widget-readout.overflow {
    /* Overflowing Readout */

    /* From Material Design Lite
        shadow-key-umbra-opacity: 0.2;
        shadow-key-penumbra-opacity: 0.14;
        shadow-ambient-shadow-opacity: 0.12;
     */
    -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                        0 3px 1px -2px rgba(0, 0, 0, 0.14),
                        0 1px 5px 0 rgba(0, 0, 0, 0.12);

    -moz-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                     0 3px 1px -2px rgba(0, 0, 0, 0.14),
                     0 1px 5px 0 rgba(0, 0, 0, 0.12);

    box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.2),
                0 3px 1px -2px rgba(0, 0, 0, 0.14),
                0 1px 5px 0 rgba(0, 0, 0, 0.12);
}

.widget-inline-hbox .widget-readout {
    /* Horizontal Readout */
    text-align: center;
    max-width: var(--jp-widgets-inline-width-short);
    min-width: var(--jp-widgets-inline-width-tiny);
    margin-left: var(--jp-widgets-inline-margin);
}

.widget-inline-vbox .widget-readout {
    /* Vertical Readout */
    margin-top: var(--jp-widgets-inline-margin);
    /* as wide as the widget */
    width: inherit;
}

/* Widget Checkbox Styling */

.widget-checkbox {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-checkbox input[type="checkbox"] {
    margin: 0px calc( var(--jp-widgets-inline-margin) * 2 ) 0px 0px;
    line-height: var(--jp-widgets-inline-height);
    font-size: large;
    flex-grow: 1;
    flex-shrink: 0;
    align-self: center;
}

/* Widget Valid Styling */

.widget-valid {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width-short);
    font-size: var(--jp-widgets-font-size);
}

.widget-valid i:before {
    line-height: var(--jp-widgets-inline-height);
    margin-right: var(--jp-widgets-inline-margin);
    margin-left: var(--jp-widgets-inline-margin);

    /* from the fa class in FontAwesome: https://github.com/FortAwesome/Font-Awesome/blob/49100c7c3a7b58d50baa71efef11af41a66b03d3/css/font-awesome.css#L14 */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.widget-valid.mod-valid i:before {
    content: "\f00c";
    color: green;
}

.widget-valid.mod-invalid i:before {
    content: "\f00d";
    color: red;
}

.widget-valid.mod-valid .widget-valid-readout {
    display: none;
}

/* Widget Text and TextArea Stying */

.widget-textarea, .widget-text {
    width: var(--jp-widgets-inline-width);
}

.widget-text input[type="text"], .widget-text input[type="number"]{
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-text input[type="text"]:disabled, .widget-text input[type="number"]:disabled, .widget-textarea textarea:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

.widget-text input[type="text"], .widget-text input[type="number"], .widget-textarea textarea {
    box-sizing: border-box;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex-grow: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    outline: none !important;
}
    
.widget-text input[type="text"], .widget-textarea textarea {
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2);
}

.widget-text input[type="number"] {
    padding: var(--jp-widgets-input-padding) 0 var(--jp-widgets-input-padding) calc(var(--jp-widgets-input-padding) *  2);
}

.widget-textarea textarea {
    height: inherit;
    width: inherit;
}

.widget-text input:focus, .widget-textarea textarea:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

/* Widget Slider */

.widget-slider .ui-slider {
    /* Slider Track */
    border: var(--jp-widgets-slider-border-width) solid var(--jp-layout-color3);
    background: var(--jp-layout-color3);
    box-sizing: border-box;
    position: relative;
    border-radius: 0px;
}

.widget-slider .ui-slider .ui-slider-handle {
    /* Slider Handle */
    outline: none !important; /* focused slider handles are colored - see below */
    position: absolute;
    background-color: var(--jp-widgets-slider-handle-background-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-handle-border-color);
    box-sizing: border-box;
    z-index: 1;
    background-image: none; /* Override jquery-ui */
}

/* Override jquery-ui */
.widget-slider .ui-slider .ui-slider-handle:hover, .widget-slider .ui-slider .ui-slider-handle:focus {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border: var(--jp-widgets-slider-border-width) solid var(--jp-widgets-slider-active-handle-color);
}

.widget-slider .ui-slider .ui-slider-handle:active {
    background-color: var(--jp-widgets-slider-active-handle-color);
    border-color: var(--jp-widgets-slider-active-handle-color);
    z-index: 2;
    transform: scale(1.2);
}

.widget-slider  .ui-slider .ui-slider-range {
    /* Interval between the two specified value of a double slider */
    position: absolute;
    background: var(--jp-widgets-slider-active-handle-color);
    z-index: 0;
}

/* Shapes of Slider Handles */

.widget-hslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    margin-left: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    top: 0;
}

.widget-vslider .ui-slider .ui-slider-handle {
    width: var(--jp-widgets-slider-handle-size);
    height: var(--jp-widgets-slider-handle-size);
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / -2 + var(--jp-widgets-slider-border-width));
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-handle-size)) / 2 - var(--jp-widgets-slider-border-width));
    border-radius: 50%;
    left: 0;
}

.widget-hslider .ui-slider .ui-slider-range {
    height: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-top: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

.widget-vslider .ui-slider .ui-slider-range {
    width: calc( var(--jp-widgets-slider-track-thickness) * 2 );
    margin-left: calc((var(--jp-widgets-slider-track-thickness) - var(--jp-widgets-slider-track-thickness) * 2 ) / 2 - var(--jp-widgets-slider-border-width));
}

/* Horizontal Slider */

.widget-hslider {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);

    /* Override the align-items baseline. This way, the description and readout
    still seem to align their baseline properly, and we don't have to have
    align-self: stretch in the .slider-container. */
    align-items: center;
}

.widgets-slider .slider-container {
    overflow: visible;
}

.widget-hslider .slider-container {
    height: var(--jp-widgets-inline-height);
    margin-left: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-right: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    flex: 1 1 var(--jp-widgets-inline-width-short);
}

.widget-hslider .ui-slider {
    /* Inner, invisible slide div */
    height: var(--jp-widgets-slider-track-thickness);
    margin-top: calc((var(--jp-widgets-inline-height) - var(--jp-widgets-slider-track-thickness)) / 2);
    width: 100%;
}

/* Vertical Slider */

.widget-vbox .widget-label {
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-vslider {
    /* Vertical Slider */
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vslider .slider-container {
    flex: 1 1 var(--jp-widgets-inline-width-short);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    margin-top: calc(var(--jp-widgets-slider-handle-size) / 2 - 2 * var(--jp-widgets-slider-border-width));
    display: flex;
    flex-direction: column;
}

.widget-vslider .ui-slider-vertical {
    /* Inner, invisible slide div */
    width: var(--jp-widgets-slider-track-thickness);
    flex-grow: 1;
    margin-left: auto;
    margin-right: auto;
}

/* Widget Progress Styling */

.progress-bar {
    -webkit-transition: none;
    -moz-transition: none;
    -ms-transition: none;
    -o-transition: none;
    transition: none;
}

.progress-bar {
    height: var(--jp-widgets-inline-height);
}

.progress-bar {
    background-color: var(--jp-brand-color1);
}

.progress-bar-success {
    background-color: var(--jp-success-color1);
}

.progress-bar-info {
    background-color: var(--jp-info-color1);
}

.progress-bar-warning {
    background-color: var(--jp-warn-color1);
}

.progress-bar-danger {
    background-color: var(--jp-error-color1);
}

.progress {
    background-color: var(--jp-layout-color2);
    border: none;
    box-shadow: none;
}

/* Horisontal Progress */

.widget-hprogress {
    /* Progress Bar */
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    align-items: center;

}

.widget-hprogress .progress {
    flex-grow: 1;
    margin-top: var(--jp-widgets-input-padding);
    margin-bottom: var(--jp-widgets-input-padding);
    align-self: stretch;
    /* Override bootstrap style */
    height: initial;
}

/* Vertical Progress */

.widget-vprogress {
    height: var(--jp-widgets-vertical-height);
    width: var(--jp-widgets-inline-width-tiny);
}

.widget-vprogress .progress {
    flex-grow: 1;
    width: var(--jp-widgets-progress-thickness);
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0;
}

/* Select Widget Styling */

.widget-dropdown {
    height: var(--jp-widgets-inline-height);
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-dropdown > select {
    padding-right: 20px;
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-radius: 0;
    height: inherit;
    flex: 1 1 var(--jp-widgets-inline-width-short);
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    box-sizing: border-box;
    outline: none !important;
    box-shadow: none;
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    vertical-align: top;
    padding-left: calc( var(--jp-widgets-input-padding) * 2);
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;
    background-repeat: no-repeat;
	background-size: 20px;
	background-position: right center;
    background-image: var(--jp-widgets-dropdown-arrow);
}
.widget-dropdown > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-dropdown > select:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* To disable the dotted border in Firefox around select controls.
   See http://stackoverflow.com/a/18853002 */
.widget-dropdown > select:-moz-focusring {
    color: transparent;
    text-shadow: 0 0 0 #000;
}

/* Select and SelectMultiple */

.widget-select {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    align-items: flex-start;
}

.widget-select > select {
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    flex: 1 1 var(--jp-widgets-inline-width-short);
    outline: none !important;
    overflow: auto;
    height: inherit;

    /* Because Firefox defines the baseline of a select as the bottom of the
    control, we align the entire control to the top and add padding to the
    select to get an approximate first line baseline alignment. */
    padding-top: 5px;
}

.widget-select > select:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.wiget-select > select > option {
    padding-left: var(--jp-widgets-input-padding);
    line-height: var(--jp-widgets-inline-height);
    /* line-height doesn't work on some browsers for select options */
    padding-top: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
    padding-bottom: calc(var(--jp-widgets-inline-height)-var(--jp-widgets-font-size)/2);
}



/* Toggle Buttons Styling */

.widget-toggle-buttons {
    line-height: var(--jp-widgets-inline-height);
}

.widget-toggle-buttons .widget-toggle-button {
    margin-left: var(--jp-widgets-margin);
    margin-right: var(--jp-widgets-margin);
}

.widget-toggle-buttons .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Radio Buttons Styling */

.widget-radio {
    width: var(--jp-widgets-inline-width);
    line-height: var(--jp-widgets-inline-height);
}

.widget-radio-box {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    box-sizing: border-box;
    flex-grow: 1;
    margin-bottom: var(--jp-widgets-radio-item-height-adjustment);
}

.widget-radio-box label {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    font-size: var(--jp-widgets-font-size);
}

.widget-radio-box input {
    height: var(--jp-widgets-radio-item-height);
    line-height: var(--jp-widgets-radio-item-height);
    margin: 0 calc( var(--jp-widgets-input-padding) * 2 ) 0 1px;
    float: left;
}

/* Color Picker Styling */

.widget-colorpicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-colorpicker > .widget-colorpicker-input {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: var(--jp-widgets-inline-width-tiny);
}

.widget-colorpicker input[type="color"] {
    width: var(--jp-widgets-inline-height);
    height: var(--jp-widgets-inline-height);
    padding: 0 2px; /* make the color square actually square on Chrome on OS X */
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    border-left: none;
    flex-grow: 0;
    flex-shrink: 0;
    box-sizing: border-box;
    align-self: stretch;
    outline: none !important;
}

.widget-colorpicker.concise input[type="color"] {
    border-left: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
}

.widget-colorpicker input[type="color"]:focus, .widget-colorpicker input[type="text"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-colorpicker input[type="text"] {
    flex-grow: 1;
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
    background: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    flex-shrink: 1;
    box-sizing: border-box;
}

.widget-colorpicker input[type="text"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Date Picker Styling */

.widget-datepicker {
    width: var(--jp-widgets-inline-width);
    height: var(--jp-widgets-inline-height);
    line-height: var(--jp-widgets-inline-height);
}

.widget-datepicker input[type="date"] {
    flex-grow: 1;
    flex-shrink: 1;
    min-width: 0; /* This makes it possible for the flexbox to shrink this input */
    outline: none !important;
    height: var(--jp-widgets-inline-height);
    border: var(--jp-widgets-input-border-width) solid var(--jp-widgets-input-border-color);
    background-color: var(--jp-widgets-input-background-color);
    color: var(--jp-widgets-input-color);
    font-size: var(--jp-widgets-font-size);
    padding: var(--jp-widgets-input-padding) calc( var(--jp-widgets-input-padding) *  2 );
    box-sizing: border-box;
}

.widget-datepicker input[type="date"]:focus {
    border-color: var(--jp-widgets-input-focus-border-color);
}

.widget-datepicker input[type="date"]:invalid {
    border-color: var(--jp-warn-color1);
}

.widget-datepicker input[type="date"]:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Play Widget */

.widget-play {
    width: var(--jp-widgets-inline-width-short);
    display: flex;
    align-items: stretch;
}

.widget-play .jupyter-button {
    flex-grow: 1;
    height: auto;
}

.widget-play .jupyter-button:disabled {
    opacity: var(--jp-widgets-disabled-opacity);
}

/* Tab Widget */

.jupyter-widgets.widget-tab {
    display: flex;
    flex-direction: column;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    /* Necessary so that a tab can be shifted down to overlay the border of the box below. */
    overflow-x: visible;
    overflow-y: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar > .p-TabBar-content {
    /* Make sure that the tab grows from bottom up */
    align-items: flex-end;
    min-width: 0;
    min-height: 0;
}

.jupyter-widgets.widget-tab > .widget-tab-contents {
    width: 100%;
    box-sizing: border-box;
    margin: 0;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    padding: var(--jp-widgets-container-padding);
    flex-grow: 1;
    overflow: auto;
}

.jupyter-widgets.widget-tab > .p-TabBar {
    font: var(--jp-widgets-font-size) Helvetica, Arial, sans-serif;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab {
    flex: 0 1 var(--jp-widgets-horizontal-tab-width);
    min-width: 35px;
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + var(--jp-border-width));
    line-height: var(--jp-widgets-horizontal-tab-height);
    margin-left: calc(-1 * var(--jp-border-width));
    padding: 0px 10px;
    background: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    border-bottom: none;
    position: relative;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current {
    color: var(--jp-ui-font-color0);
    /* We want the background to match the tab content background */
    background: var(--jp-layout-color1);
    min-height: calc(var(--jp-widgets-horizontal-tab-height) + 2 * var(--jp-border-width));
    transform: translateY(var(--jp-border-width));
    overflow: visible;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab.p-mod-current:before {
    position: absolute;
    top: calc(-1 * var(--jp-border-width));
    left: calc(-1 * var(--jp-border-width));
    content: '';
    height: var(--jp-widgets-horizontal-tab-top-border);
    width: calc(100% + 2 * var(--jp-border-width));
    background: var(--jp-brand-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:first-child {
    margin-left: 0;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tab:hover:not(.p-mod-current) {
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon {
    margin-left: 4px;
}

.jupyter-widgets.widget-tab > .p-TabBar .p-mod-closable > .p-TabBar-tabCloseIcon:before {
    font-family: FontAwesome;
    content: '\f00d'; /* close */
}

.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabIcon,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabLabel,
.jupyter-widgets.widget-tab > .p-TabBar .p-TabBar-tabCloseIcon {
    line-height: var(--jp-widgets-horizontal-tab-height);
}

/* Accordion Widget */

.p-Collapse {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Collapse-header {
    padding: var(--jp-widgets-input-padding);
    cursor: pointer;
    color: var(--jp-ui-font-color2);
    background-color: var(--jp-layout-color2);
    border: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    padding: calc(var(--jp-widgets-container-padding) * 2 / 3) var(--jp-widgets-container-padding);
    font-weight: bold;
}

.p-Collapse-header:hover {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
}

.p-Collapse-open > .p-Collapse-header {
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color0);
    cursor: default;
    border-bottom: none;
}

.p-Collapse .p-Collapse-header::before {
    content: '\f0da\00A0';  /* caret-right, non-breaking space */
    display: inline-block;
    font: normal normal normal 14px/1 FontAwesome;
    font-size: inherit;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.p-Collapse-open > .p-Collapse-header::before {
    content: '\f0d7\00A0'; /* caret-down, non-breaking space */
}

.p-Collapse-contents {
    padding: var(--jp-widgets-container-padding);
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border-left: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-right: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    border-bottom: var(--jp-widgets-border-width) solid var(--jp-border-color1);
    overflow: auto;
}

.p-Accordion {
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.p-Accordion .p-Collapse {
    margin-bottom: 0;
}

.p-Accordion .p-Collapse + .p-Collapse {
    margin-top: 4px;
}



/* HTML widget */

.widget-html, .widget-htmlmath {
    font-size: var(--jp-widgets-font-size);
}

.widget-html > .widget-html-content, .widget-htmlmath > .widget-html-content {
    /* Fill out the area in the HTML widget */
    align-self: stretch;
    flex-grow: 1;
    flex-shrink: 1;
    /* Makes sure the baseline is still aligned with other elements */
    line-height: var(--jp-widgets-inline-height);
    /* Make it possible to have absolutely-positioned elements in the html */
    position: relative;
}


/* Image widget  */

.widget-image {
    max-width: 100%;
    height: auto;
}
</style><style type="text/css">/* Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
</style><link id="favicon" type="image/x-icon" rel="shortcut icon" href="http://localhost:8888/static/base/images/favicon-notebook.ico"></head>

<body class="notebook_app command_mode" data-jupyter-api-token="79df47a3f65c664f6e71d314de63e88f2a8afb1f51e42b68" data-base-url="/" data-ws-url="" data-notebook-name="Untitled.ipynb" data-notebook-path="Desktop/Untitled.ipynb" dir="ltr"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=79df47a3f65c664f6e71d314de63e88f2a8afb1f51e42b68" title="dashboard">
      <img src="./21大数据张兆鹤-二元函数梯度下降_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  


<span id="save_widget" class="save_widget">
    <span id="notebook_name" class="filename">二元函数梯度下降</span>
    <span class="checkpoint_status" title="没有检查点"></span>
    <span class="autosave_status">（已自动保存）</span>
</span>


  

<span id="kernel_logo_widget">
  
  <img class="current_kernel_logo" alt="Current Kernel Logo" src="./21大数据张兆鹤-二元函数梯度下降_files/logo-64x64.png" title="Python 3 (ipykernel)" style="display: inline;">
  
</span>


  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  
<div id="menubar-container" class="container">
<div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <button type="button" class="btn btn-default navbar-btn navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <i class="fa fa-bars"></i>
              <span class="navbar-text">Menu</span>
            </button>
            <p id="kernel_indicator" class="navbar-text indicator_area">
              <span class="kernel_indicator_name">Python 3 (ipykernel)</span>
              <i id="kernel_indicator_icon" class="kernel_idle_icon" title="内核空闲"></i>
            </p>
            <i id="readonly-indicator" class="navbar-text" title="This notebook is read-only" style="display: none;">
                <span class="fa-stack">
                    <i class="fa fa-save fa-stack-1x"></i>
                    <i class="fa fa-ban fa-stack-2x text-danger"></i>
                </span>
            </i>
            <i id="modal_indicator" class="navbar-text modal_indicator" title="命令模式"></i>
            <span id="notification_area"><div id="notification_kernel" class="notification_widget btn btn-xs navbar-btn undefined info" style="display: none;"><span></span></div><div id="notification_notebook" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div><div id="notification_trusted" class="notification_widget btn btn-xs navbar-btn" role="button" style=""><span title="Javascript disabled for notebook display">不可信</span></div><div id="notification_widgets" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></span>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" id="filelink" data-toggle="dropdown" aria-haspopup="true" aria-controls="file_menu">File</a>
                    <ul id="file_menu" class="dropdown-menu" role="menu" aria-labelledby="filelink">
                        <li id="new_notebook" class="menu_focus_highlight dropdown dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">New Notebook<span class="sr-only">Dropdown</span></a>
                            <ul class="dropdown-menu" id="menu-new-notebook-submenu" role="menu">
                            <li id="new-notebook-submenu-python3"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Python 3 (ipykernel)</a></li></ul>
                        </li>
                        <li id="open_notebook" role="none" title="Opens a new window with the Dashboard view">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Open...</a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="copy_notebook" role="none" title="Open a copy of this notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Make a Copy...</a></li>
                        <li id="save_notebook_as" role="none" title="Save a copy of the notebook&#39;s contents and start a new kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Save as...</a></li>
                        <li id="rename_notebook" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Rename...</a></li>
                        <li id="save_checkpoint" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Save and Checkpoint</span><span class="kb"><kbd>Ctrl-S</kbd></span></a></li>
                        <!-- <hr/> -->
                        <li class="divider" role="none"></li>
                        <li id="restore_checkpoint" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Revert to Checkpoint<span class="sr-only">Dropdown</span></a>
                          <ul class="dropdown-menu"><li class="disabled"><a>没有检查点</a></li></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="print_preview" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Print Preview</a></li>
                        <li class="dropdown-submenu menu_focus_highlight" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Download as<span class="sr-only">Dropdown</span></a>
                            <ul id="download_menu" class="dropdown-menu">
                                
                                <li id="download_asciidoc">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">AsciiDoc (.asciidoc)</a>
                                </li>
                                
                                <li id="download_html">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">HTML (.html)</a>
                                </li>
                                
                                <li id="download_latex">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">LaTeX (.tex)</a>
                                </li>
                                
                                <li id="download_markdown">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Markdown (.md)</a>
                                </li>
                                
                                <li id="download_notebook">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Notebook (.ipynb)</a>
                                </li>
                                
                                <li id="download_pdf">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">PDF via LaTeX (.pdf)</a>
                                </li>
                                
                                <li id="download_rst">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">reST (.rst)</a>
                                </li>
                                
                                <li id="download_script">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Python (.py)</a>
                                </li>
                                
                                <li id="download_slides">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Reveal.js slides (.slides.html)</a>
                                </li>
                                
                                <li id="download_webpdf">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">PDF via HTML (.pdf)</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li class="dropdown-submenu hidden" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Deploy as</a>
                            <ul id="deploy_menu" class="dropdown-menu"></ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="trust_notebook" role="none" title="Trust the output of this notebook">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">信任笔记本</a></li>
                        <li class="divider" role="none"></li>
                        <li id="close_and_halt" role="none" title="Shutdown this notebook&#39;s kernel, and close this window">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Close and Halt</a></li>
                    </ul>
                </li>

                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" id="editlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="edit_menu">Edit</a>
                    <ul id="edit_menu" class="dropdown-menu" role="menu" aria-labelledby="editlink">
                        <li id="cut_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Cut Cells</span><span class="kb"><kbd>X</kbd></span></a></li>
                        <li id="copy_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Copy Cells</span><span class="kb"><kbd>C</kbd></span></a></li>
                        <li id="paste_cell_above" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Above</span><span class="kb"><kbd>Shift-V</kbd></span></a></li>
                        <li id="paste_cell_below" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Paste Cells Below</span><span class="kb"><kbd>V</kbd></span></a></li>
                        <li id="paste_cell_replace" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true">Paste Cells &amp; Replace</a></li>
                        <li id="delete_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Delete Cells</span><span class="kb"><kbd>D</kbd>,<kbd>D</kbd></span></a></li>
                        <li id="undelete_cell" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true" class="menu-shortcut-container"><span class="action">Undo Delete Cells</span><span class="kb"><kbd>Z</kbd></span></a></li>
                        <li class="divider" role="none"></li>
                        <li id="split_cell" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Split Cell</span><span class="kb"><kbd>Ctrl-Shift-Minus</kbd></span></a></li>
                        <li id="merge_cell_above" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Merge Cell Above</a></li>
                        <li id="merge_cell_below" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Merge Cell Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="move_cell_up" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Move Cell Up</a></li>
                        <li id="move_cell_down" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Move Cell Down</a></li>
                        <li class="divider" role="none"></li>
                        <li id="edit_nb_metadata" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Edit Notebook Metadata</a></li>
                        <li class="divider" role="none"></li>
                        <li id="find_and_replace" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem"> Find and Replace </a></li>
                        <li class="divider" role="none"></li>
                        <li id="cut_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Cut Cell Attachments</a></li>
                        <li id="copy_cell_attachments" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Copy Cell Attachments</a></li>
                        <li id="paste_cell_attachments" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true">Paste Cell Attachments</a></li>
                        <li class="divider" role="none"></li>
                        <li id="insert_image" class="disabled" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-disabled="true">  Insert Image </a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" id="viewlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="view_menu">View</a>
                    <ul id="view_menu" class="dropdown-menu" role="menu" aria-labelledby="viewlink">
                        <li id="toggle_header" role="none" title="Show/Hide the logo and notebook title (above menu bar)">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Toggle Header</a>
                        </li>
                        <li id="toggle_toolbar" role="none" title="Show/Hide the action icons (below menu bar)">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Toggle Toolbar</a>
                        </li>
                        <li id="toggle_line_numbers" role="none" title="Show/Hide line numbers in cells">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Toggle Line Numbers</span><span class="kb"><kbd>Shift-L</kbd></span></a>
                        </li>
                        <li id="menu-cell-toolbar" class="menu_focus_highlight dropdown-submenu" role="none">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Toolbar</a>
                            <ul class="dropdown-menu" id="menu-cell-toolbar-submenu"><li data-name="%E6%97%A0"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">无</a></li><li data-name="%E7%BC%96%E8%BE%91%E5%85%83%E6%95%B0%E6%8D%AE"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">编辑元数据</a></li><li data-name="%E5%8E%9F%E5%A7%8B%E5%8D%95%E5%85%83%E6%A0%BC%E6%A0%BC%E5%BC%8F"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">原始单元格格式</a></li><li data-name="%E5%B9%BB%E7%81%AF%E7%89%87"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">幻灯片</a></li><li data-name="%E9%99%84%E4%BB%B6"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">附件</a></li><li data-name="Tags"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Tags</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" id="insertlink" data-toggle="dropdown" aria-haspopup="true" aria-controls="insert_menu">Insert</a>
                    <ul id="insert_menu" class="dropdown-menu" role="menu" aria-labelledby="insertlink">
                        <li id="insert_cell_above" role="none" title="Insert an empty Code cell above the currently active cell">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Above</span><span class="kb"><kbd>A</kbd></span></a></li>
                        <li id="insert_cell_below" role="none" title="Insert an empty Code cell below the currently active cell">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Insert Cell Below</span><span class="kb"><kbd>B</kbd></span></a></li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" id="celllink" data-toggle="dropdown" aria-haspopup="true" aria-controls="cell_menu">Cell</a>
                    <ul id="cell_menu" class="dropdown-menu" role="menu" aria-labelledby="celllink">
                        <li id="run_cell" role="none" title="Run this cell, and move cursor to the next one">
                            <a role="menuitem" href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Run Cells</span><span class="kb"><kbd>Ctrl-Enter</kbd></span></a></li>
                        <li id="run_cell_select_below" role="none" title="Run this cell, select below">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Select Below</span><span class="kb"><kbd>Shift-Enter</kbd></span></a></li>
                        <li id="run_cell_insert_below" role="none" title="Run this cell, insert below">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" class="menu-shortcut-container"><span class="action">Run Cells and Insert Below</span><span class="kb"><kbd>Alt-Enter</kbd></span></a></li>
                        <li id="run_all_cells" role="none" title="Run all cells in the notebook">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Run All</a></li>
                        <li id="run_all_cells_above" role="none" title="Run all cells above (but not including) this cell">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Run All Above</a></li>
                        <li id="run_all_cells_below" role="none" title="Run this cell and all cells below it">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem">Run All Below</a></li>
                        <li class="divider" role="none"></li>
                        <li id="change_cell_type" class="menu_focus_highlight dropdown-submenu" role="none" title="All cells in the notebook have a cell type. By default, new cells are created as &#39;Code&#39; cells">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Cell Type</a>
                            <ul class="dropdown-menu" role="menu">
                              <li id="to_code" role="none" title="Contents will be sent to the kernel for execution, and output will display in the footer of cell">
                                  <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Code</span><span class="kb"><kbd>Y</kbd></span></a></li>
                              <li id="to_markdown" title="Contents will be rendered as HTML and serve as explanatory text">
                                  <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Markdown</span><span class="kb"><kbd>M</kbd></span></a></li>
                              <li id="to_raw" title="Contents will pass through nbconvert unmodified">
                                  <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Raw NBConvert</span><span class="kb"><kbd>R</kbd></span></a></li>
                            </ul>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="current_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Current Outputs</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_current_output" role="none" title="Hide/Show the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Toggle</span><span class="kb"><kbd>O</kbd></span></a>
                                </li>
                                <li id="toggle_current_output_scroll" title="Scroll the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Toggle Scrolling</span><span class="kb"><kbd>Shift-O</kbd></span></a>
                                </li>
                                <li id="clear_current_output" title="Clear the output of the current cell">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                        <li id="all_outputs" class="menu_focus_highlight dropdown-submenu" role="none"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">All Output</a>
                            <ul class="dropdown-menu" role="menu">
                                <li id="toggle_all_output" role="none" title="Hide/Show the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Toggle</a>
                                </li>
                                <li id="toggle_all_output_scroll" title="Scroll the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Toggle Scrolling</a>
                                </li>
                                <li id="clear_all_output" title="Clear the output of all cells">
                                    <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Clear</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" data-toggle="dropdown" id="kernellink">Kernel</a>
                    <ul id="kernel_menu" class="dropdown-menu" aria-labelledby="kernellink">
                        <li id="int_kernel" title="Send Keyboard Interrupt (CTRL-C) to the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Interrupt</span><span class="kb"><kbd>I</kbd>,<kbd>I</kbd></span></a>
                        </li>
                        <li id="restart_kernel" title="Restart the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Restart</span><span class="kb"><kbd>0</kbd>,<kbd>0</kbd></span></a>
                        </li>
                        <li id="restart_clear_output" title="Restart the Kernel and clear all output">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Restart &amp; Clear Output</a>
                        </li>
                        <li id="restart_run_all" title="Restart the Kernel and re-run the notebook">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Restart &amp; Run All</a>
                        </li>
                        <li id="reconnect_kernel" title="Reconnect to the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Reconnect</a>
                        </li>
                        <li id="shutdown_kernel" title="Shutdown the Kernel">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Shutdown</a>
                        </li>
                        <li class="divider" role="none"></li>
                        <li id="menu-change-kernel" class="menu_focus_highlight dropdown-submenu" role="menuitem">
                            <a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle" data-toggle="dropdown">Change kernel</a>
                            <ul class="dropdown-menu" id="menu-change-kernel-submenu"><li id="kernel-submenu-python3"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Python 3 (ipykernel)</a></li></ul>
                        </li>
                    </ul>
                </li>
                <li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" data-toggle="dropdown" class="dropdown-toggle">Widgets</a><ul id="widget-submenu" class="dropdown-menu"><li title="Save the notebook with the widget state information for static rendering"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Save Notebook Widget State</a></li><li title="Clear the widget state information from the notebook"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Clear Notebook Widget State</a></li><ul class="divider"></ul><li title="Download the widget state as a JSON file"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Download Widget State</a></li><li title="Embed interactive widgets"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Embed Widgets</a></li></ul></li><li class="dropdown"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="dropdown-toggle" data-toggle="dropdown">Help</a>
                    <ul id="help_menu" class="dropdown-menu">
                        
                        <li id="notebook_tour" title="A quick tour of the notebook user interface"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">User Interface Tour</a></li>
                        <li id="keyboard_shortcuts" title="Opens a tooltip with all keyboard shortcuts"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" class="menu-shortcut-container"><span class="action">Keyboard Shortcuts</span><span class="kb"><kbd>H</kbd></span></a></li>
                        <li id="edit_keyboard_shortcuts" title="Opens a dialog allowing you to edit Keyboard shortcuts"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">Edit Keyboard Shortcuts</a></li>
                        <li class="divider"></li>
                        

						
                        
                            
                                <li><a rel="noreferrer" href="http://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Notebook Help
                                </a></li>
                            
                                <li><a rel="noreferrer" href="https://help.github.com/articles/markdown-basics/" target="_blank" title="Opens in a new window">
                                
                                    <i class="fa fa-external-link menu-icon pull-right"></i>
                                

                                Markdown
                                </a></li>
                            
                            
                        
                        <li id="kernel-help-links" class="divider"></li><li><a target="_blank" title="在新窗口打开" href="https://docs.python.org/3.9?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>Python Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="https://ipython.org/documentation.html?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>IPython Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="https://docs.scipy.org/doc/numpy/reference/?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>NumPy Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="https://docs.scipy.org/doc/scipy/reference/?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>SciPy Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="https://matplotlib.org/contents.html?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>Matplotlib Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="http://docs.sympy.org/latest/index.html?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>SymPy Reference</span></a></li><li><a target="_blank" title="在新窗口打开" href="https://pandas.pydata.org/pandas-docs/stable/?v=20241128152421"><i class="fa fa-external-link menu-icon pull-right"></i><span>pandas Reference</span></a></li><li class="divider"></li>
                        <li title="About Jupyter Notebook"><a id="notebook_about" href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#">About</a></li>
                        
                    </ul>
                </li>
              </ul>
            </div>
        </div>
    </div>
</div>

<div id="maintoolbar" class="navbar">
  <div class="toolbar-inner navbar-inner navbar-nobg">
    <div id="maintoolbar-container" class="container toolbar"><div class="btn-group" id="save-notbook"><button class="btn btn-default" title="保存并建立检查点" data-jupyter-action="jupyter-notebook:save-notebook"><i class="fa-save fa"></i></button></div><div class="btn-group" id="insert_above_below"><button class="btn btn-default" title="在下面插入代码块" data-jupyter-action="jupyter-notebook:insert-cell-below"><i class="fa-plus fa"></i></button></div><div class="btn-group" id="cut_copy_paste"><button class="btn btn-default" title="剪切选择的代码块" data-jupyter-action="jupyter-notebook:cut-cell"><i class="fa-cut fa"></i></button><button class="btn btn-default" title="复制选择的代码块" data-jupyter-action="jupyter-notebook:copy-cell"><i class="fa-copy fa"></i></button><button class="btn btn-default" title="粘贴到下面" data-jupyter-action="jupyter-notebook:paste-cell-below"><i class="fa-paste fa"></i></button></div><div class="btn-group" id="move_up_down"><button class="btn btn-default" title="上移选中单元格" data-jupyter-action="jupyter-notebook:move-cell-up"><i class="fa-arrow-up fa"></i></button><button class="btn btn-default" title="下移选中单元格" data-jupyter-action="jupyter-notebook:move-cell-down"><i class="fa-arrow-down fa"></i></button></div><div class="btn-group" id="run_int"><button class="btn btn-default" aria-label="运行" title="运行代码块, 选择下面的代码块" data-jupyter-action="jupyter-notebook:run-cell-and-select-next"><i class="fa-play fa"></i><span class="toolbar-btn-label">运行</span></button><button class="btn btn-default" title="中断内核" data-jupyter-action="jupyter-notebook:interrupt-kernel"><i class="fa-stop fa"></i></button><button class="btn btn-default" title="重启内核（带确认对话框）" data-jupyter-action="jupyter-notebook:confirm-restart-kernel"><i class="fa-repeat fa"></i></button><button class="btn btn-default" title="重启内核, 然后重新运行整个代码（带确认对话框）" data-jupyter-action="jupyter-notebook:confirm-restart-kernel-and-run-all-cells"><i class="fa-forward fa"></i></button></div><select id="cell_type" aria-label="combobox, select cell type" role="combobox" class="form-control select-xs"><option value="code">代码</option><option value="markdown">Markdown</option><option value="raw">原生 NBConvert</option><option value="heading">标题</option><option value="multiselect" disabled="disabled" style="display: none;">-</option></select><div class="btn-group" id="cmd_palette"><button class="btn btn-default" title="打开命令配置" data-jupyter-action="jupyter-notebook:show-command-palette"><i class="fa-keyboard-o fa"></i></button></div></div>
  </div>
</div>
</div>

<div class="lower-header-bar"></div>

</div>

<div id="site" style="display: block; height: 565.205px;">


<div id="ipython-main-app">
    <div id="notebook_panel">
        <div id="notebook" tabindex="-1"><div class="container" id="notebook-container"><div class="cell code_cell rendered selected" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[1]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 175.483px; left: 3.99147px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="bottom: 0px;"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 564.264px; margin-bottom: -15px; border-right-width: 35px; min-height: 861px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"><div class="CodeMirror-cursor" style="left: 3.99147px; top: 169.886px; height: 16.9886px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">matplotlib</span>.<span class="cm-property">pyplot</span> <span class="cm-keyword">as</span> <span class="cm-variable">plt</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">from</span> <span class="cm-variable">mpl_toolkits</span>.<span class="cm-property">mplot3d</span> <span class="cm-keyword">import</span> <span class="cm-variable">Axes3D</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 定义函数</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">f</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> (<span class="cm-variable">x</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>)<span class="cm-operator">*</span>(<span class="cm-variable">y</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">y</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 计算梯度</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">gradient</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">f_x</span> <span class="cm-operator">=</span> (<span class="cm-number">2</span><span class="cm-operator">*</span><span class="cm-variable">x</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>)<span class="cm-operator">*</span>(<span class="cm-variable">y</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">y</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>) <span class="cm-operator">+</span> (<span class="cm-variable">x</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>)<span class="cm-operator">*</span>(<span class="cm-number">2</span><span class="cm-operator">*</span><span class="cm-variable">y</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">f_y</span> <span class="cm-operator">=</span> (<span class="cm-number">2</span><span class="cm-operator">*</span><span class="cm-variable">y</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>)<span class="cm-operator">*</span>(<span class="cm-variable">x</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>) <span class="cm-operator">+</span> (<span class="cm-variable">y</span><span class="cm-operator">**</span><span class="cm-number">2</span> <span class="cm-operator">-</span> <span class="cm-variable">y</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>)<span class="cm-operator">*</span>(<span class="cm-number">2</span><span class="cm-operator">*</span><span class="cm-variable">x</span> <span class="cm-operator">-</span> <span class="cm-number">1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">np</span>.<span class="cm-property">array</span>([<span class="cm-variable">f_x</span>, <span class="cm-variable">f_y</span>])</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 梯度下降算法</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">def</span> <span class="cm-def">gradient_descent</span>(<span class="cm-variable">initial_point</span>, <span class="cm-variable">learning_rate</span><span class="cm-operator">=</span><span class="cm-number">0.01</span>, <span class="cm-variable">num_iterations</span><span class="cm-operator">=</span><span class="cm-number">100</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">x</span>, <span class="cm-variable">y</span> <span class="cm-operator">=</span> <span class="cm-variable">initial_point</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-variable">points</span> <span class="cm-operator">=</span> [(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>)]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">for</span> <span class="cm-variable">_</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span>(<span class="cm-variable">num_iterations</span>):</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">grad</span> <span class="cm-operator">=</span> <span class="cm-variable">gradient</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">x</span> <span class="cm-operator">-=</span> <span class="cm-variable">learning_rate</span> <span class="cm-operator">*</span> <span class="cm-variable">grad</span>[<span class="cm-number">0</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">y</span> <span class="cm-operator">-=</span> <span class="cm-variable">learning_rate</span> <span class="cm-operator">*</span> <span class="cm-variable">grad</span>[<span class="cm-number">1</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">        <span class="cm-variable">points</span>.<span class="cm-property">append</span>((<span class="cm-variable">x</span>, <span class="cm-variable">y</span>))</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;">    <span class="cm-keyword">return</span> <span class="cm-variable">points</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 初始点</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">initial_point</span> <span class="cm-operator">=</span> (<span class="cm-number">2</span>, <span class="cm-number">2</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 执行梯度下降</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">points</span> <span class="cm-operator">=</span> <span class="cm-variable">gradient_descent</span>(<span class="cm-variable">initial_point</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 绘制函数</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">x</span> <span class="cm-operator">=</span> <span class="cm-variable">np</span>.<span class="cm-property">linspace</span>(<span class="cm-operator">-</span><span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">100</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">y</span> <span class="cm-operator">=</span> <span class="cm-variable">np</span>.<span class="cm-property">linspace</span>(<span class="cm-operator">-</span><span class="cm-number">2</span>, <span class="cm-number">2</span>, <span class="cm-number">100</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">X</span>, <span class="cm-variable">Y</span> <span class="cm-operator">=</span> <span class="cm-variable">np</span>.<span class="cm-property">meshgrid</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">Z</span> <span class="cm-operator">=</span> <span class="cm-variable">f</span>(<span class="cm-variable">X</span>, <span class="cm-variable">Y</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">fig</span> <span class="cm-operator">=</span> <span class="cm-variable">plt</span>.<span class="cm-property">figure</span>()</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ax</span> <span class="cm-operator">=</span> <span class="cm-variable">fig</span>.<span class="cm-property">add_subplot</span>(<span class="cm-number">111</span>, <span class="cm-variable">projection</span><span class="cm-operator">=</span><span class="cm-string">'3d'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ax</span>.<span class="cm-property">plot_surface</span>(<span class="cm-variable">X</span>, <span class="cm-variable">Y</span>, <span class="cm-variable">Z</span>, <span class="cm-variable">cmap</span><span class="cm-operator">=</span><span class="cm-string">'viridis'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 绘制梯度下降路径</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">path_x</span>, <span class="cm-variable">path_y</span> <span class="cm-operator">=</span> <span class="cm-builtin">zip</span>(<span class="cm-operator">*</span><span class="cm-variable">points</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ax</span>.<span class="cm-property">plot</span>(<span class="cm-variable">path_x</span>, <span class="cm-variable">path_y</span>, <span class="cm-variable">f</span>(<span class="cm-variable">np</span>.<span class="cm-property">array</span>(<span class="cm-variable">path_x</span>), <span class="cm-variable">np</span>.<span class="cm-property">array</span>(<span class="cm-variable">path_y</span>)), <span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'r'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># 标出最小值点</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">min_x</span>, <span class="cm-variable">min_y</span> <span class="cm-operator">=</span> <span class="cm-variable">points</span>[<span class="cm-operator">-</span><span class="cm-number">1</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ax</span>.<span class="cm-property">scatter</span>(<span class="cm-variable">min_x</span>, <span class="cm-variable">min_y</span>, <span class="cm-variable">f</span>(<span class="cm-variable">min_x</span>, <span class="cm-variable">min_y</span>), <span class="cm-variable">color</span><span class="cm-operator">=</span><span class="cm-string">'b'</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">plt</span>.<span class="cm-property">show</span>()</span></pre></div></div></div></div></div><div style="position: absolute; height: 35px; width: 1px; border-bottom: 0px solid transparent; top: 861px;"></div><div class="CodeMirror-gutters" style="display: none; height: 896px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="点击展开输出；双击隐藏输出"></div><div class="output"><div class="output_area"><div class="run_this_cell"></div><div class="prompt"></div><div class="output_subarea output_png" dir="auto"><img src="data:image/png;base64,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"></div></div></div><div class="btn btn-default output_collapsed" title="点击展开输出" style="display: none;">. . .</div></div></div><div class="cell code_cell unselected rendered" tabindex="2"><div class="input"><div class="prompt_container"><div class="prompt input_prompt"><bdi>In</bdi>&nbsp;[&nbsp;]:</div><div class="run_this_cell" title="Run this cell"><i class="fa-step-forward fa"></i></div></div><div class="inner_cell"><div class="ctb_hideshow"><div class="celltoolbar"></div></div><div class="input_area" aria-label="Edit code here"><div class="CodeMirror cm-s-ipython"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5.59668px; left: 3.99147px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; min-width: 6.99147px; margin-bottom: -15px; border-right-width: 35px; min-height: 28px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 3.99147px; top: 0px; height: 16.9886px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 35px; width: 1px; border-bottom: 0px solid transparent; top: 28px;"></div><div class="CodeMirror-gutters" style="display: none; height: 63px;"></div></div></div></div></div></div><div class="output_wrapper"><div class="out_prompt_overlay prompt" title="点击展开输出；双击隐藏输出"></div><div class="output"></div><div class="btn btn-default output_collapsed" title="点击展开输出" style="display: none;">. . .</div></div></div></div><div class="end_space"></div></div>
        <div id="tooltip" class="ipython_tooltip" style="display:none"><div class="tooltipbuttons"><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="button" class="ui-button"><span class="ui-icon ui-icon-close">关闭</span></a><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="button" class="ui-button" id="expanbutton" title="纵向展开工具提示（按两次 Shift+Tab）"><span class="ui-icon ui-icon-plus">Expand</span></a><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="button" class="ui-button" title="在分页器中显示当前的文档字符串（按四次 Shift+Tab）"><span class="ui-icon ui-icon-arrowstop-l-n">在分页器中打开</span></a><a href="http://localhost:8888/notebooks/Desktop/%E4%BA%8C%E5%85%83%E5%87%BD%E6%95%B0%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D.ipynb#" role="button" class="ui-button" title="当您键入时，工具提示会停留十秒" style="display: none;"><span class="ui-icon ui-icon-clock">关闭</span></a></div><div class="pretooltiparrow"></div><div class="tooltiptext smalltooltip"></div></div>
    </div>
</div>



</div>



<div id="pager" class="ui-resizable">
    <div id="pager-contents">
        <div id="pager-container" class="container"></div>
    </div>
    <div id="pager-button-area"><a role="button" title="在外部窗口打开分页器" class="ui-button"><span class="ui-icon ui-icon-extlink"></span></a><a role="button" title="关闭分页器" class="ui-button"><span class="ui-icon ui-icon-close"></span></a></div>
<div class="ui-resizable-handle ui-resizable-n" style="z-index: 90;"></div></div>






<script type="text/javascript">
    sys_info = {"notebook_version": "6.4.5", "notebook_path": "C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\notebook", "commit_source": "", "commit_hash": "", "sys_version": "3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)]", "sys_executable": "C:\\ProgramData\\Anaconda3\\python.exe", "sys_platform": "win32", "platform": "Windows-10-10.0.19044-SP0", "os_name": "nt", "default_encoding": "utf-8"};
</script>

<script src="./21大数据张兆鹤-二元函数梯度下降_files/encoding.js.下载" charset="utf-8"></script>

<script src="./21大数据张兆鹤-二元函数梯度下降_files/main.min.js.下载" type="text/javascript" charset="utf-8"></script>



<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


<div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal;"></div></div></body></html>