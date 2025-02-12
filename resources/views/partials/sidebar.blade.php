<!-- resources/views/partials/sidebar.blade.php -->
<div id="draggable-sidebar" class="bg-white w-64 p-6 shadow-lg rounded-lg h-auto fixed top-6 left-6 cursor-move">
    <h2 class="text-xl font-bold text-blue-600 mb-6">Menu</h2>
    <ul class="space-y-4">
        <!-- Add Section Button -->
        <li>
            <button class="flex items-center text-gray-700 hover:text-blue-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                Add section
            </button>
        </li>
        <!-- Rearrange Button -->
        <li>
            <button class="flex items-center text-gray-700 hover:text-blue-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
                Rearrange
            </button>
        </li>
        <!-- Design & Font Button -->
        <li>
            <button class="flex items-center text-gray-700 hover:text-blue-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a4 4 0 11-8 0 4 4 0 018 0zM12 20c-3.313 0-7-2.687-7-6s2.687-6 6-6 6 2.687 6 6-2.687 6-6 6z"></path></svg>
                Design & Font
            </button>
        </li>
        <!-- Download Button -->
        <li>
            <button class="flex items-center text-gray-700 hover:text-blue-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h8a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V7"></path></svg>
                Download
            </button>
        </li>
        <!-- Share Button -->
        <li>
            <button class="flex items-center text-gray-700 hover:text-blue-600">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
                Share
            </button>
        </li>
    </ul>
</div>

<script>
    // Make the sidebar draggable
    document.addEventListener('DOMContentLoaded', function () {
        const sidebar = document.getElementById('draggable-sidebar');
        let isDragging = false;
        let offsetX = 0;
        let offsetY = 0;

        // Mouse down event to start dragging
        sidebar.addEventListener('mousedown', function (e) {
            isDragging = true;
            offsetX = e.clientX - sidebar.getBoundingClientRect().left;
            offsetY = e.clientY - sidebar.getBoundingClientRect().top;
            sidebar.style.cursor = 'grabbing';
        });

        // Mouse move event to move the sidebar
        document.addEventListener('mousemove', function (e) {
            if (isDragging) {
                const x = e.clientX - offsetX;
                const y = e.clientY - offsetY;
                sidebar.style.left = `${x}px`;
                sidebar.style.top = `${y}px`;
            }
        });

        // Mouse up event to stop dragging
        document.addEventListener('mouseup', function () {
            isDragging = false;
            sidebar.style.cursor = 'move';
        });
    });
</script>