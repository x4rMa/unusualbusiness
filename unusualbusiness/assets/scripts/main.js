/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

console.log('Hello, World!');

(function() {
  $(document).ready(function() {
    $('.slider').unslider({
      keys: false,
      arrows: false,
      nav: true});
  });
})();
