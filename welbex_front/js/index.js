const API_URL =
    "http://localhost:8000/home/";


async function fetchAPI(url) {
  try {
    const response = await fetch(url);
    let data = await response.json();

    paginationCount = Math.ceil(data.count / pageSize);

    hideloader();
    initPagination()
    show(data);
  } catch (e) {
    console.log(e)
  }
}

fetchAPI(API_URL)


function hideloader() {
  document.getElementById('loading').style.display = 'none';
}

function show(data) {

  let tab =
      `<tr>
          <th>Date</th>
          <th>Name</th>
          <th>Amount</th>
          <th>Distance</th>
         </tr>`;

  // Loop to access all rows
  for (let r of data.results) {
    tab += `<tr>
    <td>${r.date} </td>
    <td>${r.name}</td>
    <td>${r.amount}</td>
    <td>${r.distance}</td>
</tr>`;
  }
  // Setting innerHTML as tab variable
  document.getElementById("table").innerHTML = tab;
}
