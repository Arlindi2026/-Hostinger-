// Estimate form: compose the request as a WhatsApp message.
(function () {
  var form = document.getElementById('estimate-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = form.dataset;
    var val = function (id) { return document.getElementById(id).value.trim(); };
    var lines = [d.intro, ''];
    [['lName', 'f-name'], ['lPhone', 'f-phone'], ['lPlace', 'f-place'], ['lService', 'f-service'], ['lDetails', 'f-details']]
      .forEach(function (p) { var v = val(p[1]); if (v) lines.push(d[p[0]] + ': ' + v); });
    window.open(form.action + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
  });
})();
