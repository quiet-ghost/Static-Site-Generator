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
