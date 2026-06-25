from rich.console import Console
from rich.panel import Panel
from rich import box
from src.graph import build_graph

console = Console()

def main() -> None:
    console.print("[yellow]Program started[/yellow]")
    issue_url = input("Enter Github issue URL: ").strip()

    graph = build_graph()

    try:
        result = graph.invoke({"issue_url": issue_url})
    except Exception as error:
        console.print(f"[red]Error:[/red] {error}")
        return
    
    console.print(
        Panel.fit(
            f"[bold]Repository:[/bold] {result['owner']}/{result['repo']}\n"
            f"[bold]Issue:[/bold] #{result['issue_number']}\n"
            f"[bold]Title:[/bold] {result['issue_title']}",
            title="Github Issue",
            border_style="green",
            box=box.ASCII,
        )
    )
    console.print(
        Panel(
            result["implementation_plan"],
            title="Implementation Plan",
            border_style="blue",
            box=box.ASCII,
        )
    )

if __name__ == "__main__":
    main()