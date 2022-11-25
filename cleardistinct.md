cleardistinct
[[https://lh3.googleusercontent.com/a/ALm5wu3TJs6-tGxwLsC0AIYV8o8wOdkos4ACyWrz8HHbJg=s96-c#.png]]

 25 yo
 live in Tokyo
 Master's Student of Univ. Tokyo (major in Philosophy)

[[cleardistinct.icon]]

code:script.js
 import '/api/code/wordbook/livepreview/script.js'
 function livepreview_init() {
 	$("a").addClass("livepreview"); 
    	$(".livepreview").livePreview({
           trigger: 'hover',
           viewWidth: 500,  
           viewHeight: 300,  
           targetWidth: 1000,  
           targetHeight: 800,  
           //scale: '0.5', 
           //offset: 50,
           position: 'bottom'
   	});
   	//$(".livepreview").livePreview();
  };
  
  const observer = new MutationObserver((mutation)=>{
   	livepreview_init();
  });
  observer.observe(document.querySelector('.page'), {childList: true, subtree: true});
   
    
  $(document).ready( e => {
   	livepreview_init();
  });
   
  var $appRoot = $('#app-container');
  $appRoot.on('click', e => {
   	livepreview_init();
  });
  
  //(function($) {
    $.fn.extend({
       livePreview: function(options) {
           
           var defaults = {
               trigger: 'hover',
               targetWidth : 1000,
               targetHeight: 800,
               viewWidth: 300,
               viewHeight: 200,
               position: 'right',
               positionOffset: 40,
           };
  
           var options = $.extend(defaults, options);
           //calculate appropriate scaling based on width.
           var scale_w = (options.viewWidth / options.targetWidth);
           var scale_h = (options.viewHeight / options.targetHeight);
           var scale_f = 1;
           var preview_id = 'livepreview_dialog';
  
           if(typeof options.scale != 'undefined')
               scale_f = options.scale;
           else
           {
               if(scale_w > scale_h)
                   scale_f = scale_w;
               else
                   scale_f = scale_h;
           }
           
           var showPreview = function(event) {
         		
               var triggerType = event.data.triggerType;
               var obj = event.data.target;
               var href = event.data.href;
               var s = event.data.scale;
               
               if( (triggerType == 'click') && ($('#' + preview_id).length == 0) ) {
                   event.preventDefault();
               }
  
               var currentPos = options.position;
                if(obj.attr("data-position"))
                   currentPos = obj.attr("data-position");
  
               var currentOffset = options.positionOffset;
               if(obj.attr("data-positionOffset"))
                   currentOffset = obj.attr("data-positionOffset");
  
               if(obj.attr("data-scale"))
                   s = obj.attr("data-scale");
  
               var pos = $(this).offset();
               var width = $(this).width();
               var height = $(this).height();
               var toppos = pos.top - (options.viewHeight/2);
               var leftpos = pos.left + width + currentOffset;
  
               if(currentPos == 'left') {
                  leftpos = pos.left - options.viewWidth - currentOffset;
               }
              
               if(currentPos == 'top') {
                  leftpos = pos.left + (width/2) - (options.viewWidth/2);
                  toppos = pos.top - options.viewHeight - currentOffset;
               }
  
               if(currentPos == 'bottom') {
                  leftpos = pos.left + (width/2) - (options.viewWidth/2);
                  toppos = pos.top + (height/2) + currentOffset;
               }
               
               //hover on 
               $('body').append('<div id="livepreview_dialog" class="' + currentPos + '" style="display:none; padding:0px; left: ' + leftpos + 'px; top:' + toppos + 'px; width: ' + options.viewWidth + 'px; height: ' + options.viewHeight + 'px"><div class="livepreview-container" style="overflow:hidden; width: ' + options.viewWidth + 'px; height: ' + options.viewHeight + 'px"><iframe id="livepreview_iframe" src="' + href + '" style="height:' + options.targetHeight + 'px; width:' + options.targetWidth + 'px;-moz-transform: scale('+ s + ');-moz-transform-origin: 0 0;-o-transform: scale('+ s + ');-o-transform-origin: 0 0;-webkit-transform: scale('+ s + ');-webkit-transform-origin: 0 0;"></iframe></div></div>');
               $('#' + preview_id).fadeIn(100);
           };
  
           return this.each(function() {
              var o = options;
              var s = scale_f;
              var obj = $(this);
              var href = obj.attr("data-preview-url") || obj.attr("href");
              var triggerType = options.trigger;
  
              if(obj.attr("data-trigger")) {
                  triggerType = obj.attr("data-trigger");
              }
  
              if(triggerType != 'click') {
                  triggerType = 'mouseenter';
                  obj.on('click', function() {
                      $('#' + preview_id).remove();
                  });
              }
              
              obj.on(triggerType, null, { triggerType: triggerType, target: obj, href: href, scale: s }, showPreview);
              obj.on('mouseleave', function() {
                  $('#' + preview_id).remove();
              });
  
           });
       }
    });
  //})(jQuery);
 
 

code:style.css
 
 code:style.css
  /*** Styles for Live Preview Window ***/
  
  #livepreview_iframe {
      box-shadow: inset 5px 5px 10px #666;
      -moz-box-shadow: inset 5 5px 10px #666;
      -webkit-box-shadow: inset 5 5px 10px #666;
  }
  
  #livepreview_dialog {
      padding:0px;
      height:200px;  
      width:300px;
      background-color:#fff;
      background-image:url('https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/18839/5d8154ec-88d8-5ce6-24a2-57f44c20a0ce.gif');
      background-image:url('/images/icon_loading.gif');
      background-repeat:no-repeat;
      background-position:center center;
      position:absolute;
      border:solid 5px #666;
      border-radius:5px;
      -moz-border-radius: 5px;
      -webkit-border-radius:5px;
  }
  
  #livepreview_dialog:after, #livepreview_dialog:before {
      border: solid transparent;
      content: " ";
      height: 0;
      width: 0;
      position: absolute;
      pointer-events: none;
  }
  
  #livepreview_dialog.bottom:after, #livepreview_dialog.bottom:before {
      bottom: 100%;
      left: 50%;
  }
  
  #livepreview_dialog.bottom:after {
      border-color: rgba(255, 255, 255, 0);
      border-bottom-color: #ffffffff;
      border-width: 20px; 
      margin-left: -20px;
  }
  #livepreview_dialog.bottom:before {
      border-color: rgba(102, 102, 102, 0);
      border-bottom-color: #666666;
      border-width: 26px;
      margin-left: -26px;
  }
  
  #livepreview_dialog.top:after, #livepreview_dialog.top:before {
      top: 100%;
      left: 50%;
  }
  
  #livepreview_dialog.top:after {
      border-color: rgba(255, 255, 255, 0);
      border-top-color: #ffffffff;
      border-width: 20px;
      margin-left: -20px;
  }
  
  #livepreview_dialog.top:before {
      border-color: rgba(102, 102, 102, 0);
      border-top-color: #666666;
      border-width: 26px;
      margin-left: -26px;
  }
  
  #livepreview_dialog.right:after, #livepreview_dialog.right:before {
      right: 100%;
      top: 50%;
  }
  
  #livepreview_dialog.right:after {
      border-color: rgba(255, 255, 255, 0);
      border-right-color: #ffffffff;
      border-width: 20px;
      margin-top: -20px;
  }
  
  #livepreview_dialog.right:before {
      border-color: rgba(102, 102, 102, 0);
      border-right-color: #666666;
      border-width: 26px;
      margin-top: -26px;
  }
  
  #livepreview_dialog.left, #livepreview_dialog.left:before {
      left: 100%;
      top: 50%;
  }
  
  #livepreview_dialog.left:after {
      border-color: rgba(255, 255, 255, 0);
      border-left-color: #ffffffff;
      border-width: 20px;
      margin-top: -20px;
  }
  
  #livepreview_dialog.left:before {
      border-color: rgba(102, 102, 102, 0);
      border-left-color: #666666;
      border-width: 26px;
      margin-top: -26px;
  }
  