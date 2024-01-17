const date = new Date();
const formattedDate = date.toLocaleDateString('en-GB', {
  year: 'numeric',
  month: 'numeric',
  day: '2-digit'
});

console.log(formattedDate); 