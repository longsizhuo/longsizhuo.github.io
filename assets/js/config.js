// config.js
import Pjax from 'pjax-api';
// or
const { Pjax } = window['pjax-api'];

new Pjax({
    areas: [
        // Try the first query.
        '#header, #primary',
        // Retry using the second query
        // if the first query doesn't match.
        '#container',
        // Retry.
        'body'
    ]
});

/*将#menu中的a的链接的页面，只取回class=pjax元素中的内容，替换掉当前页面class=pjax元素中的内容*/
$(document).pjax('.#menu a', '.pjax', {fragment:'.pjax', timeout:8000});


$(document).on({
    'pjax:click': function() {
//点击链接时，需要触发的事件写到这里
    },
    'pjax:start': function() {
//当开始获取请求时，需要触发的事件写在这里
    },
    'pjax:end': function() {
//当请求完成后，需要触发的事件写在这里
    }
});