from src.call_tool import decide_retrival_tool, decide_ingenstion_tool


def agent():
    try:
        user_input = str(input("Do you want to Ingestion data (Y/N) : "))
        if not user_input:
            raise ValueError("User Input should not empty")
        else:
            if "N" == user_input:
                decide_retrival_tool()
            elif "Y" == user_input:
                decide_ingenstion_tool()
    except Exception as e:
        print("[app] Agent failed:", e)
