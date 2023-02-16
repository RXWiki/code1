$(document).ready(function() {

            $('#yes').on('click', function() {
            $value = $('#value').text();
            $.ajax({
                url: `${Number($value)}/yes`,
                type: 'POST',
                data: {
                   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val()
                },
                success: function() {
                    window.location = `${Number($value) + 1}`
                    console.log("nice!")
                }
            });
            });

            $('#no').on('click', function() {
            $value = $('#value').text();
            $.ajax({
                url: `${Number($value)}/no`,
                type: 'POST',
                data: {
                   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val()
                },
                success: function() {
                    window.location = `${Number($value) + 1}`
                    console.log("nice!")
                }
            });
            });

        });