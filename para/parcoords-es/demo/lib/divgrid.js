// http://bl.ocks.org/3687826
d3.divgrid = function(config) {
  console.log(config)
  var columns = [];

  var dg = function(selection) {
    if (columns.length == 0)  columns = d3.keys(config) //d3.keys(selection.data()[0][0]);
    console.log(config);

    // header
    selection.selectAll(".header")
        .data([true])
      .enter().append("div")
        .attr("class", "header")
    selection.selectAll(".grow-div")
        .data([true])
      .enter().append("div")
        .attr("class", "grow-div")
    
    var header = selection.select(".header")
      .selectAll(".cell")
      .data(columns);

    header.enter().append("div")
      .attr("class", function(d,i) { return "col-" + i; })
      .classed("cell", true)

    selection.selectAll(".header .cell")
      .text(function(d) { return d; });

    header.exit().remove();

    // rows
    var rows = selection.select(".grow-div").selectAll(".grow")
        .data(function(d) { return d; })

    rows.enter().append("div")
        .attr("class", "grow")

    rows.exit().remove();

    var cells = selection.selectAll(".grow").selectAll(".cell")
        .data(function(d) { return columns.map(function(col){return d[col];}) })

    // cells
    cells.enter().append("div")
      .attr("class", function(d,i) { return "col-" + i; })
      .classed("cell", true)

    cells.exit().remove();

    selection.selectAll(".cell")
      .text(function(d) { return d; });

    return dg;
  };

  dg.columns = function(_) {
    if (!arguments.length) return columns;
    columns = _;
    return this;
  };

  return dg;
};
