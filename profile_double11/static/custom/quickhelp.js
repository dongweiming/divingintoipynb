define([
    'base/js/namespace',
    'jquery',
    'base/js/dialog',
], function(IPython, $, dialog) {
    var QuickHelp = function () {
        var cmd_ctrl = 'Cmd-';
        var cm_shortcuts = [
            { shortcut:"Ctrl-w",   help:"kill-region" },
            { shortcut:"Ctrl-k",   help:"kill-line" },
            { shortcut:"Ctrl-y",   help:"yank" },
            { shortcut:"Ctrl-Space",   help:"start-mark" },
            { shortcut:"Ctrl-f",   help:"forward-char" },
            { shortcut:"Ctrl-b",   help:"backward-char" },
            { shortcut:"Ctrl-d",   help:"delete-char after current" },
            { shortcut:"Ctrl-i",   help:"delete-char before current" },
            { shortcut:"Ctrl-n",   help:"next-line" },
            { shortcut:"Ctrl-p",   help:"previous-line" },
            { shortcut:"Ctrl-a",   help:"go-line-start" },
            { shortcut:"Ctrl-e",   help:"go-line-end" },
            { shortcut:"Ctrl-Up",   help:"backward-paragraph" },
            { shortcut:"Ctrl-Down",   help:"forward-paragraph" },
            { shortcut:"Ctrl-o",   help:"open-new-line" },
            { shortcut:"Ctrl-t",   help:"transpose-chars" },
            { shortcut:"Cmd-/",   help:"comment-uncomment" },
            { shortcut:"Cmd-z",   help:"undo" },
            { shortcut:"Ctrl-s",   help:"find-next" },
            { shortcut:"Ctrl-r",   help:"find-prev" },
            { shortcut:"Ctrl-g",   help:"quit" },
            { shortcut:"Ctrl-j",   help:"newline-and-indent" },
            { shortcut:"Ctrl-x Ctrl-s",   help:"save" },
            { shortcut:"Ctrl-x s",   help:"save-all" },
            { shortcut:"Ctrl-x f",   help:"open" },
            { shortcut:"Ctrl-x u",   help:"undo" },
            { shortcut:"Ctrl-x Tab",   help:"indentUnit" },
            { shortcut:"Alt-w",   help:"copy-to-ring" },
            { shortcut:"Alt-b",   help:"backward-word" },
            { shortcut:"Alt-f",   help:"forward-word" },
            { shortcut:"Alt-d",   help:"delete-word before current" },
            { shortcut:"Alt-Backspace",   help:"delete-char after current" },
            { shortcut:"Alt-a",   help:"go-sentence-start" },
            { shortcut:"Alt-e",   help:"go-sentence-end" },
            { shortcut:"Alt-k",   help:"kill sentence" },
            { shortcut:"Alt-v",   help:"scroll-down" },
            { shortcut:"Ctrl-v",   help:"scroll-up" },
            { shortcut:"Alt-l",   help:"make-upper after current" },
            { shortcut:"Alt-u",   help:"make-lower after current" },
            { shortcut:"Alt-;",   help:"comment-uncomment" },
            { shortcut:"Ctrl-Alt-k",   help:"delete-expr after current" },
            { shortcut:"Ctrl-Alt-Backspace",   help:"delete-expr before current" },
            { shortcut:"Ctrl-Alt-f",   help:"forward-expr" },
            { shortcut:"Ctrl-Alt-b",   help:"backward-expr" },
            { shortcut:"Shift-Alt-,",   help:"go-doc-start" },
            { shortcut:"Shift-Alt-.",   help:"go-doc-end" },
            { shortcut:"Shift-Alt-5",   help:"replace" },
            { shortcut:"Alt-g g",   help:"goto line" },
            { shortcut:"Ctrl-h b",   help:"display keyboard shortcuts" },
        ]


        var humanize_map = {
            // http://apple.stackexchange.com/questions/55727/
            'cmd':'⌘',
            'shift':'⇧',
            'alt':'⌥',
            'up':'↑',
            'down':'↓',
            'left':'←',
            'right':'→',
            'eject':'⏏',
            'tab':'⇥',
            'backtab':'⇤',
            'capslock':'⇪',
            'esc':'⎋',
            'ctrl':'⌃',
            'enter':'↩',
            'pageup':'⇞',
            'pagedown':'⇟',
            'home':'↖',
            'end':'↘',
            'altenter':'⌤',
            'space':'␣',
            'delete':'⌦',
            'backspace':'⌫',
            'apple': '',
        };

        function humanize_key(key){
            if (key.length === 1){
                key = key.toUpperCase();
            }
            return humanize_map[key.toLowerCase()]||key;
        }

        function humanize_sequence(sequence){
            var joinchar = ',';
            var hum = _.map(sequence.replace(/meta/g, 'cmd').split(','), humanize_shortcut).join(joinchar);
            return hum;
        }

        function humanize_shortcut(shortcut){
            var joinchar = '';
            var sh = _.map(shortcut.split('-'), humanize_key ).join(joinchar);
            return sh;
        }

        QuickHelp.prototype.show_keyboard_shortcuts = function () {
            var that = this;
            if ( this.shortcut_dialog ){
                // if dialog is already shown, close it
                $(this.shortcut_dialog).modal("toggle");
                return;
            }

            var help, shortcut;
            var i, half, n;
            var element = $('<div/>');

            var cmd_div = this.build_command_help();
            element.append(cmd_div);

            this.shortcut_dialog = dialog.modal({
                title : "Emacs Keyboard shortcuts",
                body : element,
                destroy : false,
                buttons : {
                    Close : {}
                },
                notebook: null,
                keyboard_manager: null,
            });
            this.shortcut_dialog.addClass("modal_stretch");
        };

        QuickHelp.prototype.build_command_help = function () {
            return build_div('<h4>press <code>Esc</code> to quit</h4>', cm_shortcuts);
        };

        var special_case = { pageup: "PageUp", pagedown: "Page Down", 'minus': '-' };

        var build_one = function (s) {
            var help = s.help;
            var shortcut = '';
            if(s.shortcut){
                shortcut = prettify(humanize_sequence(s.shortcut));
            }
            return $('<div>').addClass('quickhelp').
                append($('<span/>').addClass('shortcut_key').append($(shortcut))).
                append($('<span/>').addClass('shortcut_descr').text(' : ' + help));

        };

        var build_div = function (title, shortcuts) {
            var i, half, n;
            var div = $('<div/>').append($(title));
            var sub_div = $('<div/>').addClass('hbox');
            var col1 = $('<div/>').addClass('box-flex1');
            var col2 = $('<div/>').addClass('box-flex1');
            n = shortcuts.length;
            half = ~~(n/2);  // Truncate :)
            for (i=0; i<half; i++) { col1.append( build_one(shortcuts[i]) ); }
            for (i=half; i<n; i++) { col2.append( build_one(shortcuts[i]) ); }
            sub_div.append(col1).append(col2);
            div.append(sub_div);
            return div;
        };

        var prettify = function (s) {
            s = s.replace(/-$/, 'minus'); // catch shortcuts using '-' key
            var keys = s.split('-');
            var k, i;
            for (i=0; i < keys.length; i++) {
                k = keys[i];
                if ( k.length == 1 ) {
                    keys[i] = "<code><strong>" + k + "</strong></code>";
                    continue; // leave individual keys lower-cased
                }
                if (k.indexOf(',') === -1){
                    keys[i] = ( special_case[k] ? special_case[k] : k.charAt(0).toUpperCase() + k.slice(1) );
                }
                keys[i] = "<code><strong>" + keys[i] + "</strong></code>";
            }
            return keys.join('-');
        };
    }
    return {'QuickHelp': QuickHelp};
})
