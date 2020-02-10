(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    
    
    try {
    
        $('#input-start').daterangepicker({
            ranges: true,
            format: "yyyy",
            viewMode: "years",
            minViewMode: "years",
            autoApply: true,
            applyButtonClasses: false,
            autoUpdateInput: false
        },function (start) {
            $('#input-start').val(start.format('YYYY'));
        });

         $('#input-end').daterangepicker({
            ranges: true,
            autoApply: true,
            applyButtonClasses: false,
            autoUpdateInput: false
        },function (end) {
            $('#input-end').val(end.format('YYYY'));
        });
    
    
    } catch(er) {console.log(er);}
    /*==================================================================
        [ Input Number ]*/
    
    try {
    
        var inputCon = $('.js-number-input');
    
        inputCon.each(function () {
            var that = $(this);
    
            var btnPlus = that.find('.plus');
            var btnMinus = that.find('.minus');
            var qtyInput = that.find('.quantity');
    
    
            btnPlus.on('click', function () {
                var oldValue = parseInt(qtyInput.val());
                var newVal = oldValue + 1;
                qtyInput.val(refineString(newVal));
            });
    
            btnMinus.on('click', function () {
                var min = 0;
    
                var oldValue = parseInt(qtyInput.val());
                if (oldValue <= min) {
                    var newVal = oldValue;
                } else {
                    var newVal = oldValue - 1;
                }
                qtyInput.val(refineString(newVal));
            });
        });
    
        function refineString(s) {
            if(parseInt(s) <= 1) return parseInt(s);
            else return parseInt(s);
        }
    
    }catch (e) {
        console.log(e);
    }

})(jQuery);