import vk_api

vk_accounts = []

print("██╗░░░██╗██╗░░██╗░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░████████╗")
print("██║░░░██║██║░██╔╝░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗╚══██╔══╝")
print("╚██╗░██╔╝█████═╝░░╚██╗████╗██╔╝██║██╔██╗██║██████╦╝██║░░██║░░░██║░░░")
print("░╚████╔╝░██╔═██╗░░░████╔═████║░██║██║╚████║██╔══██╗██║░░██║░░░██║░░░")
print("░░╚██╔╝░░██║░╚██╗░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╦╝╚█████╔╝░░░██║░░░")
print("░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░")
print("𝗩𝗞𝗪𝗶𝗻𝗕𝗼𝘁 v1\n\nАвтор: @radeberlc\nМодификация скрипта и загрузка его в публичные источники разрешена при условии указания автора.\nБот предназначен для конкурсов в группах, а точнее повышения шанса выиграть за счет комментариев и лайков аккаунтов указанных в файле скрипта.")

__postid__ = int(input("[?] Айди поста: "))
__ownerid__ = int(input("[?] Айди страницы: "))

vk_items = len(vk_accounts)

def postComment(account):
    try:
        login = account.split(":")[0]
        pwd = account.split(":")[1]
        vk_session = vk_api.VkApi(login, pwd)
        vk_session.auth()
        vk = vk_session.get_api()
        vk.wall.createComment(owner_id=__ownerid__, post_id=__postid__,message='тест')
        vk.likes.add(type="post", owner_id=__ownerid__, item_id=__postid__)
        print("[+] VKWinBot: Успешно!")
    except:
        print("[-] VKWinBot: Произошла неудача :(")


if __name__ == "__main__":
    for i in range(vk_items):
        postComment(vk_accounts[i])

    print("[+] VKWinBot: Завершил работу!")
