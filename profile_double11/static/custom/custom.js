require.config({

    baseUrl: '/static/',
    paths: {
        nbextensions : '/nbextensions',
        kernelspecs : '/kernelspecs',
        underscore : 'components/underscore/underscore-min',
        backbone : 'components/backbone/backbone-min',
        jquery: 'components/jquery/jquery.min',
        bootstrap: 'components/bootstrap/js/bootstrap.min',
        bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
        jqueryui: 'components/jquery-ui/ui/minified/jquery-ui.min',
        moment: 'components/moment/moment',
        codemirror: 'components/codemirror',
        termjs: 'components/term.js/src/term',
        selectize: 'components/selectize/selectize',
        emacs: 'components/codemirror/emacs',
    },
    shim: {
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
        jqueryui: {
            deps: ["jquery"],
            exports: "$"
        },
        selectize: {
            deps: ["jquery"]
        }
    }
});

require(["widgets/js/widget", "widgets/js/manager", "jquery", "selectize"], function(widget, manager, $){
    var SelectizeView = widget.DOMWidgetView.extend({

        render : function(){
            var theme = this.model.get('theme');
            $('head').append('<link rel="stylesheet" href="/static/custom/selectize.' + theme + '.css">');
            this.$el
                .addClass('widget-hbox widget-selectize');
            this.$label = $('<label></label>')
                .appendTo(this.$el)
                .addClass('widget-hlabel')
                .attr('for', 'input-selectize')
                .hide();
            this.$listbox = $('<input/>')
                .addClass(theme)
                .addClass('widget-listbox')
                .attr('id', 'input-selectize')
                .attr('type', 'text')
                .attr('value', this.model.get('_value_names').join(','))
                .appendTo(this.$el);
            this.update();
        },

        update : function(options){
            if (options === undefined || options.updated_view != this) {
                var description = this.model.get('description'),
                    disabled = this.model.get('disabled');
                this.$listbox.prop('disabled', disabled);
                if (description.length === 0) {
                    this.$label.hide();
                } else {
                    this.$label.show();
                    this.$label.text(description);
                }

                this.$listbox.selectize({
                    persist: false,
                    createOnBlur: true,
                    create: true
                });
                return SelectizeView.__super__.update.apply(this);
            }
        },

        events: {
            "change input" : "handleChanged"
        },

        handleChanged : function(e) { // handle_click
            this.model.set('value_name', e.target.value, {updated_view: this});
            this.touch();
        }
    });

    manager.WidgetManager.register_widget_view('SelectizeView', SelectizeView);
})

require(["base/js/events", "emacs"], function(events){
    events.on('app_initialized.NotebookApp', function(){
        mode = 'emacs';
        IPython.notebook.get_cells().map(function (c) {
            return c.code_mirror.setOption('keyMap', mode);
        });

        IPython.Cell.options_default.cm_config.keyMap = mode;

        // exentensions from IPython-notebook-extensions
        IPython.load_extensions('slidemode/main');
        IPython.load_extensions('usability/chrome_clipboard');
        IPython.load_extensions('usability/dragdrop/drag-and-drop');
        IPython.load_extensions('usability/runtools/runtools');
        IPython.load_extensions('usability/rubberband/main');
        IPython.load_extensions('usability/toggle_full_textarea/main');
    });
})
