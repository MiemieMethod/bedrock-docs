document$.subscribe(function() {
  // 选择所有具有 class "md-tabs__link" 的 <a> 标签
  const links = document.querySelectorAll('a.md-tabs__link');

  links.forEach(link => {
    // 查找当前 <a> 标签下的 <span>，且具有 class "md-nav__link md-nav__link--active"
    const activeSpan = link.querySelector('span.md-nav__link.md-nav__link--active');

    if (activeSpan) {
      // 获取 activeSpan 内的所有子节点（例如 <span class="twemoji"> 和 <span class="md-ellipsis">）
      const childNodes = activeSpan.childNodes;

      // 将这些子节点移动到 <a> 标签下
      childNodes.forEach(node => {
        link.appendChild(node.cloneNode(true));
      });

      // 移除原来的 activeSpan
      link.removeChild(activeSpan);
    }
});
})