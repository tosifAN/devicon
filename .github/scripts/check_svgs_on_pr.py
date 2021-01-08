import sys
import time


# pycharm complains that build_assets is an unresolved ref
# don't worry about it, the script still runs
from build_assets import filehandler, arg_getters
from build_assets import github_env, svg_checker


def main():
    """
    Check the quality of the svgs.
    If any error is found, set an environmental variable called SVG_ERR_MSGS
    that will contains the error messages.
    """
    args = arg_getters.get_check_svgs_on_pr_args()
    try:
        # check the svgs
        svgs = filehandler.get_added_modified_svgs(args.files_changed_json_path)
        print("SVGs to check: ", *svgs, sep='\n')
        svg_checker.check_svgs(svgs)
        print("All SVGs found were good. Task completed.")
    except Exception as e:
        github_env.set_env_var("SVG_ERR_MSGS", str(e))
        sys.exit(str(e))


if __name__ == "__main__":
    main()
