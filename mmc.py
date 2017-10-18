from yast import *

class MMC:
    @staticmethod
    def __GenericDialog__():
        return VBox(
            Id('mainDialog'),
            ReplacePoint(Id('topmenu'), Empty()),
            HBox(
                HSpacing(1),
                VBox(
                    VSpacing(0.2),
                    HBox(
                        Heading(Id('title'), Opt('hstretch'), "Initializing ..."),
                        HStretch(),
                        ReplacePoint(Id('relnotes_rp'), Empty())
                    ),
                    VWeight(
                        1,
                        HVCenter(Opt('hvstretch'), ReplacePoint(Id('contents'), Empty()))
                    )
                ),
                HSpacing(1)
            ),
            ReplacePoint(Id('rep_button_box'), MMC.__buttons()),
            VSpacing(0.2)
        )

    @staticmethod
    def __buttons():
        return HBox(
            HWeight(1, ReplacePoint(Id('rep_back'),
                PushButton(Id('back'), Opt('key_F8'), 'Back')
            )),
            HStretch(),
            HWeight(1, ReplacePoint(Id('rep_next'),
                PushButton(Id('next'), Opt('key_F10', 'default'), 'Next')
            )),
        )

    @staticmethod
    def AddMenu(*menus):
        contents = Left(HBox(*menus))
        UI.ReplaceWidget('topmenu', contents)

    @staticmethod
    def CreateDialog():
        """Create a new MMC Dialog

        Synopsis
        CreateDialog()
        """
        content = MMC.__GenericDialog__()
        UI.OpenDialog(content, Opt('mainDialog'))

    @staticmethod
    def SetPlugin(title, contents):
        """Set the plugin container within the main frame

        Synopsis
        SetPlugin(title, contents)

        Parameters
        title  The title of the window
        contents  The widget contents of the main frame
        """
        UI.ChangeWidget('title', 'Value', String(title))
        UI.ReplaceWidget('contents', contents)

    @staticmethod
    def DisableBackButton():
        pass

    @staticmethod
    def DisableNextButton():
        pass

    @staticmethod
    def EnableNextButton():
        pass

    @staticmethod
    def DisableAbortButton():
        pass


    @staticmethod
    def CloseDialog():
        UI.CloseDialog()

