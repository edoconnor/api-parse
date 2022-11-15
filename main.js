fetch("dow30.json")
  .then((resp)=> {
    if(!resp.ok) throw new Error(resp.statusText);
    return resp.json();
  })
  .then(([first, second, ...rest]) => {
    console.log(first.Symbol);
    console.log(second.CIK);
  })
  .catch(log);