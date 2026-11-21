class HTMLNode:
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        children: list[str] | None,
        props: dict[str, str] | None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method must be implemented in subclasses")

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        if self.props is None:
            return ""

        return " ".join(
            f'href={key}:"target={value}"' for key, value in self.props.items()
        )

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag is None:
            return self.value or ""

        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("ParentNode must have children")

        children_html = "".join(
            child.to_html() if isinstance(child, HTMLNode) else str(child)
            for child in self.children
        )
        props_html = self.props_to_html()
        opening_tag = f"<{self.tag}"

        if props_html:
            opening_tag += f" {props_html}"
        opening_tag += ">"

        return f"{opening_tag}{children_html}</{self.tag}>"
