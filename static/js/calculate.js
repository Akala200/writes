 //base discount
    var discount = 2.5;
    //overall discount apllied on total cart value
    var totalDiscount = 25;

//function to calculate price
    function getPrice() {
//get the price of assignment
        var getCoursePrice = $('#courses Option:selected').attr("data-price");
        //get the urgency of assignment
        var getDuration = $('#duration Option:selected').val();
        //get the standard of assignment
        var getTime = $('#class Option:selected').val();
        //get page value of assignment
        var getStudents = $('#students Option:selected').val();

        //using switch statement to determine which course with price
        switch (getCoursePrice) {
            case '22.96':
            //base price of course
                var basePrice = 22.96;
                //if statements to add additional discount depending on urgency
                if (getDuration < 2) {
                    //alert("working till here");
                    var totalPrice = (basePrice + (getTime * basePrice / 100)) * getStudents;
                    $('#price').html(totalPrice.toFixed(2));
                    //alert(getStudents);
                    //25% off price here
                    var discountedPrice = totalPrice - (totalDiscount * totalPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                    //alert (totalPrice);
                } else
                if (getDuration < 11) {
                    var increment = 2.1;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 21) {
                    var increment = 1.4;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 35) {
                    var increment = 1.1;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 80) {
                    var increment = 0.8;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                }
                break;
//second case statement
            case '38.54':
                var basePrice = 38.54;
                if (getDuration < 2) {
                    //alert("working till here");
                    var totalPrice = (basePrice + (getTime * basePrice / 100)) * getStudents;
                    $('#price').html(totalPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = totalPrice - (totalDiscount * totalPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                    //alert (discountedPrice);
                } else
                if (getDuration < 11) {
                    var increment = 2.1;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 21) {
                    var increment = 1.4;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 35) {
                    var increment = 1.1;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                } else
                if (getDuration < 80) {
                    var increment = 0.8;
                    var extraDiscount = getDuration * increment + discount;
                    console.log(increment + " for " + extraDiscount);
                    var totalPrice = (basePrice + (getTime * basePrice / 100));
                    var extraDiscountedPrice = (totalPrice - (extraDiscount * totalPrice / 100)) * getStudents;
                    $('#price').html(extraDiscountedPrice.toFixed(2));
                    //25% off price here
                    var discountedPrice = extraDiscountedPrice - (totalDiscount * extraDiscountedPrice / 100);
                    $('#discountedPrice').html(discountedPrice.toFixed(2));
                }

                break;



        }
    }


    //basic script to load function on page load and change
    $(document).ready(function () {
        getPrice();
        $('select').change(function () {


            getPrice();
        });
    });