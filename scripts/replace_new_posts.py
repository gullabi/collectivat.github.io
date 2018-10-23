import os
import yaml

def main():
    filename = 'scripts/portfolio.yml'
    new_posts = yaml.load(open(filename))
    for key in new_posts.keys():
        target_filename = key.replace(':description','')
        source_path = os.path.join('_posts', target_filename)
        target_path = os.path.join('_new_posts', target_filename)
        with open(target_path, 'w') as out:
            for line in open(source_path).readlines():
                if line.startswith('description'):
                    out.write('description: "%s"\n'%new_posts[key])
                else:
                    out.write(line)

if __name__ == "__main__":
    main()
