require([
    'underscore',
    'jquery',
    'splunkjs/mvc',
    'splunkjs/mvc/tableview',
    'splunkjs/mvc/simplexml/ready!'
], function(_, $, mvc, TableView) {

    var CustomLinkRenderer = TableView.BaseCellRenderer.extend({
        canRender: function(cell) {
            return cell.field === 'link';
        },
        render: function($td, cell) {
            var link = cell.value;

            var a = $('<a target="_blank">').attr("href", cell.value).text("URL");

            $td.addClass('table-link').empty().append(a);
                              
            a.click(function(e) {
              e.preventDefault();
              window.location = $(e.currentTarget).attr('href');
              // or for popup:
              // window.open($(e.currentTarget).attr('href'));
            });

        }
    });
	var CustomLinkRenderer1 = TableView.BaseCellRenderer.extend({
        canRender: function(cell) {
            return cell.field === 'brow_info';
        },
        render: function($td, cell) {
            var link = cell.value;

            var a = $('<a target="_blank">').attr("href", cell.value).text("Details");

            $td.addClass('table-link').empty().append(a);
                              
            a.click(function(e) {
              window.open(this.href, "","width=1002,height=700,location=0,menubar=0,scrollbars=1,status=1,resizable=0")
				e.preventDefault(); // Or: return false;
              // or for popup:
              // window.open($(e.currentTarget).attr('href'));
            });

        }
    });
        
        // Get the table view by id
    mvc.Components.get('link').getVisualization(function(tableView){
        // Register custom cell renderer, the table will re-render automatically
        tableView.addCellRenderer(new CustomLinkRenderer());
		tableView.addCellRenderer(new CustomLinkRenderer1());
    });

});
