def convert_to_mermaid(flowchart_text: str):

    steps = [step.strip() for step in flowchart_text.split("→")]

    mermaid_lines = []
    mermaid_lines.append("flowchart TD")

    for i in range(len(steps) - 1):
        current_node = f"N{i}[{steps[i]}]"
        next_node = f"N{i+1}[{steps[i+1]}]"
        mermaid_lines.append(f"{current_node} --> {next_node}")

    return "\n".join(mermaid_lines)