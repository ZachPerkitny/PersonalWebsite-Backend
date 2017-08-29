from django.core.management.base import BaseCommand
from blog.posts.models import Post


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def _create_posts(self, n):
        for i in range(n):
            post = Post(
                title="It's a fucking test",
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent at commodo metus, vitae commodo metus. Sed accumsan non tortor eu ultricies. Curabitur vulputate diam sit amet nibh tempus fermentum. Suspendisse vitae placerat leo. Sed et finibus augue. Mauris erat arcu, lacinia sed aliquet in, commodo vehicula leo. Duis lacus diam, dictum eu convallis in, lobortis quis massa. Proin semper tempor nibh, vitae pulvinar augue laoreet eget. Vestibulum nec enim risus."
                        "Fusce odio magna, porta non porta sodales, aliquet et sapien. Mauris in turpis rhoncus, facilisis tellus in, accumsan risus. Duis iaculis luctus ex non faucibus. Donec condimentum leo quis ligula tempus, sollicitudin laoreet quam consequat. Vestibulum venenatis rutrum mauris ac tempor. Morbi laoreet libero ut tempor ullamcorper. Sed vel erat tincidunt, fringilla eros ut, cursus mi. Proin tempus id velit non eleifend. Aenean ut porttitor massa. Nullam quis viverra felis. Quisque ut elementum tortor. Praesent bibendum, est sit amet imperdiet consequat, lorem justo tincidunt massa, quis sodales sapien elit eu odio. Etiam aliquet, lorem vitae iaculis lacinia, nibh mauris volutpat enim, et consectetur nunc nisi a massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ac odio lacinia, hendrerit arcu id, fringilla sem. Nam faucibus ut nisi vel sagittis."
                        "Integer tempus hendrerit augue, sed semper tortor pharetra quis. Quisque vitae justo quis justo iaculis consequat consequat sit amet elit. Ut sodales consequat mauris sit amet porta. Nulla ut maximus lacus. Sed porttitor viverra magna, eu mattis ante ultricies ut. Maecenas sagittis tincidunt arcu quis tempus. Morbi quis arcu scelerisque, convallis urna non, suscipit turpis. Nunc mattis, ipsum non interdum imperdiet, nunc nisl efficitur odio, quis varius elit nibh ut neque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed sodales, est quis cursus dignissim, quam arcu rutrum augue, eu mollis nulla arcu in ipsum."
                        "Nunc ut erat finibus, consequat leo id, dapibus massa. Nullam quis neque ligula. In finibus, velit non auctor interdum, nunc ipsum laoreet ipsum, a porttitor nibh purus ac orci. Nullam id purus ante. Suspendisse a congue justo. Mauris laoreet turpis non ultricies pulvinar. Aenean consequat ultricies risus, sit amet efficitur mi tempus eget. Nam at porta ligula. Vestibulum placerat congue ex, eget sagittis enim eleifend et. Vivamus et odio eu mi suscipit sollicitudin eget nec leo."
                        "In urna lacus, consectetur ac risus ut, iaculis tincidunt felis. Integer mattis ex vel nunc mattis, eu accumsan metus volutpat. Nulla quis rutrum nibh. Nulla luctus lacus eros, ut rhoncus lorem porttitor et. Nulla quis mi vitae felis porta scelerisque. Proin non pellentesque sapien. Aenean quis feugiat nisl, sit amet commodo tellus. Sed aliquet nisl et lacus sagittis, nec pulvinar mauris viverra. Ut ultrices arcu velit, vel vulputate nibh semper quis. Nunc et pellentesque metus. Aenean molestie turpis ac neque rutrum, vitae tincidunt lacus aliquam. Suspendisse maximus luctus lectus ac sollicitudin. Integer ac tellus a lorem feugiat imperdiet ut ut ipsum. Duis vitae ipsum at ipsum tincidunt pulvinar. Donec accumsan mauris eget ultrices ullamcorper. Aenean a ligula a sapien molestie bibendum."
            )
            post.save()

    def handle(self, *args, **options):
        self._create_posts(options['n'])
