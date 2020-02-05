import logging
from gi.repository import GLib

import guizero

from code_snippets import big_button_project

logger = logging.getLogger('BigButton')
loop = GLib.MainLoop()


def refresh_app():
    score.value = big_game.score
    # print(big_game.btn_active)
    if big_game.game_active:
        button.text = 'Running...'
        active.bg = big_game.btn_active
    else:
        button.text = 'Start'
        active.bg = 'lightgray'
    app.update()
    return True


def end_app():
    logger.info('Game Exit!!!!')
    big_game.game_exit()
    app.destroy()
    loop.quit()


if __name__ == '__main__':
    logger.debug('Debug On!!!!')
    app = guizero.App("Big Button Project",
                      layout='grid',
                      width=600,
                      height=300)
    big_game = big_button_project.ButtonGame()
    title = guizero.Text(app, text='Big Button Game', size=24, grid=[0, 1])
    button = guizero.PushButton(app, big_game.game_start,
                                text='Start', grid=[1, 1])
    active = guizero.TextBox(app, text='', width=20, grid=[2, 1])
    active.bg = big_game.btn_active
    score_lbl = guizero.Text(app, text='Score:', size=36, grid=[3, 0])
    score = guizero.Text(app, text=big_game.score, size=36, grid=[3, 2])
    game_over = guizero.PushButton(app, end_app, text='Exit', grid=[4, 1])

    GLib.idle_add(refresh_app)
    try:
        loop.run()
    except KeyboardInterrupt:
        end_app()
