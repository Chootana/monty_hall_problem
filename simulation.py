import random 
import matplotlib.pyplot as plt


def run(num_door=3, max_count=1000):
    cnt_changed = 0
    cnt_unchanged = 0
    p_changed = []
    p_unchanged = []

    for _ in range(max_count):
        truth = random.randrange(num_door)
        player_selected = random.randrange(num_door)
        doors_unselected = [door for door in range(num_door) if door is not player_selected]

        if player_selected == truth:
            door_another = random.choice(doors_unselected)
        else:
            door_another = truth
        
        if door_another == truth:
            cnt_changed += 1
        elif player_selected == truth:
            cnt_unchanged += 1
        else:
            assert False, 'truth door missing!'
        
        total = cnt_changed + cnt_unchanged
        p_changed.append(cnt_changed / total)
        p_unchanged.append(cnt_unchanged / total)

    print('cnt_changed: {}, p_changed: {}'.format(cnt_changed, p_changed[-1]))
    print('cnt_unchanged: {}, p_unchanged: {}'.format(cnt_unchanged, p_unchanged[-1]))

    plt.plot(p_changed, label='p_changed_win')
    plt.plot(p_unchanged, label='p_unchanged_win')
    plt.legend()
    plt.savefig('./result.png')        

if __name__ == '__main__':
    run()