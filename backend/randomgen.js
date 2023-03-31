[
  '{{repeat(5, 7)}}',
  {
    product_id: '{{index()}}',
    productName : '{{lorem(2,"words")}}',
    productOwnerName : '{{firstName()}} {{surname()}}',
    Developers : ['{{repeat(1,5)}}',
                  '{{firstName()}} {{surname()}}'
                 ],
    scrumMasterName : '{{firstName()}} {{surname()}}',
    startDate: '{{date(new Date(2014, 0, 1), new Date(), "YYYY-MM-dd")}}',
    methodology: '{{random("Agile", "Waterfall")}}'
  }
]