(function($) {
  $(document).on('content-editor:ready', function() {
    ContentEditor.addPluginButton(
      'pages_richtext',
      '<i class="fa fa-pencil"></i>'
    );
    ContentEditor.addPluginButton(
      'pages_image',
      '<i class="fa fa-image"></i>'
    );
  });
})(django.jQuery);
